#include "Field.h"
#include "Objects.h"
#include "Physics.h"
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>

void Physics::Physics::objects(std::vector<Objects::Object> objects) {
    objectlist = objects;
};

void Physics::Physics::boundary(std::vector<Field::Field> boundaries) {
    boundarylist = boundaries;
};

std::vector<Objects::Object> Physics::Physics::getObjects() {
    return objectlist;
};

std::vector<Field::Field> Physics::Physics::getBoundaries() {
    return boundarylist;
};

void Physics::Physics::update(float dt) {
    //Update positions according to new velocity and acceleration
    for (int i = 0; i < objectlist.size(); i++) {
        objectlist[i].updatePos(objectlist[i].getPos()[0] + (objectlist[i].getDeriv()[0] * dt), objectlist[i].getPos()[1] + (objectlist[i].getDeriv()[1] * dt));
        objectlist[i].updateDeriv(objectlist[i].getDeriv()[0] + (objectlist[i].getDeriv()[2] * dt), objectlist[i].getDeriv()[1] + (objectlist[i].getDeriv()[3] * dt), objectlist[i].getDeriv()[2] * 0.8f, objectlist[i].getDeriv()[3] * 0.8f);
    };
    //Check for collision
    collisionCheck();
};

void Physics::Physics::collisionCheck() {
    //Check collision between boundaries and objects
    
    //Check collision between object and object
    for (int i = 0; i < objectlist.size(); i++) {
        for (int j = 0; j < objectlist.size(); j++) {
            if (i != j) {
                if (fabs((double)((double)objectlist[i].getPos()[0] - (double)objectlist[j].getPos()[0]) * (double)(objectlist[i].getPos()[0] - (double)objectlist[j].getPos()[0]) + ((double)objectlist[i].getPos()[1] - (double)objectlist[j].getPos()[1]) * (objectlist[i].getPos()[1] - objectlist[j].getPos()[1])) <= (double)((double)objectlist[i].getStat()[1] + (double)objectlist[j].getStat()[1]) * (double)((double)objectlist[i].getStat()[1] + (double)objectlist[j].getStat()[1])) {
                    bounceBall(&objectlist[i], &objectlist[j]);
                    displaceBalls(&objectlist[i], &objectlist[j]);
                };
            };
        };
        for (int k = 0; k < boundarylist.size(); k++) {
            float fLineX1 = boundarylist[k].getPos()[2] - boundarylist[k].getPos()[0];
            float fLineY1 = boundarylist[k].getPos()[3] - boundarylist[k].getPos()[1];

            float fLineX2 = objectlist[i].getPos()[0] - boundarylist[k].getPos()[0];
            float fLineY2 = objectlist[i].getPos()[1] - boundarylist[k].getPos()[1];

            float fEdgeLength = fLineX1 * fLineX1 + fLineY1 * fLineY1;

            float t = std::max(0.0f, std::min(fEdgeLength, (fLineX1 * fLineX2 + fLineY1 * fLineY2))) / fEdgeLength;

            float fClosestPointX = boundarylist[k].getPos()[0] + t * fLineX1;
            float fClosestPointY = boundarylist[k].getPos()[1] + t * fLineY1;

            float fDistance = sqrtf((objectlist[i].getPos()[0] - fClosestPointX) * (objectlist[i].getPos()[0] - fClosestPointX) + (objectlist[i].getPos()[1] - fClosestPointY) * (objectlist[i].getPos()[1] - fClosestPointY));

            if (fDistance <= (objectlist[i].getStat()[1])) {
                Objects::Object fakeBall;

                fakeBall.set(objectlist[i].getStat()[0], 1.0f, 1.0f, fClosestPointX, fClosestPointY, -1.0f * objectlist[i].getDeriv()[0], -1.0f * objectlist[i].getDeriv()[1], 0.0f, 0.0f);

                // Store Fake Ball
                fakeObjectlist.push_back(fakeBall);

                // Calculate displacement required
                float fOverlap = 1.0f * (fDistance - objectlist[i].getStat()[1] - 1);

                // Displace Current Ball away from collision
                objectlist[i].updatePos(objectlist[i].getPos()[0] - fOverlap * (objectlist[i].getPos()[0] - fClosestPointX) / fDistance, objectlist[i].getPos()[1] - fOverlap * (objectlist[i].getPos()[1] - fClosestPointY) / fDistance);

                bounceBall(&objectlist[i], &fakeBall);
            };
        };
    };
};

void Physics::Physics::displaceBalls(Objects::Object *ball, Objects::Object *target) {
    // Distance between ball centers
    float fDistance = sqrtf((ball->getPos()[0] - target->getPos()[0]) * (ball->getPos()[0] - target->getPos()[0]) + (ball->getPos()[1] - target->getPos()[1]) * (ball->getPos()[1] - target->getPos()[1]));

    // Calculate displacement required
    float fOverlap = 0.5f * (fDistance - ball->getStat()[1] - target->getStat()[1]);

    // Displace Current Ball away from collision
    ball->updatePos(ball->getPos()[0] - fOverlap * (ball->getPos()[0] - target->getPos()[0]) / fDistance, ball->getPos()[1] - fOverlap * (ball->getPos()[1] - target->getPos()[1]) / fDistance);

    // Displace Target Ball away from collision
    target->updatePos(target->getPos()[0] - fOverlap * (target->getPos()[0] - ball->getPos()[0]) / fDistance, target->getPos()[1] - fOverlap * (target->getPos()[1] - ball->getPos()[1]) / fDistance);
};

void Physics::Physics::bounceBall(Objects::Object *ball, Objects::Object *target) {
    //Handle collision between object and object

    //Get distance 
    float distance = sqrtf((ball->getPos()[0] - target->getPos()[0]) * (ball->getPos()[0] - target->getPos()[0]) + (ball->getPos()[1] - target->getPos()[1]) * (ball->getPos()[1] - target->getPos()[1]));

    //Get Normal vector
    float nx = (target->getPos()[0] - ball->getPos()[0]) / distance;
    float ny = (target->getPos()[1] - ball->getPos()[1]) / distance;

    //Tangent vector
    float tx = -ny;
    float ty = nx;

    //Dot product for Tangent
    float dpTan1 = ball->getDeriv()[0] * tx + ball->getDeriv()[1] * ty;
    float dpTan2 = target->getDeriv()[0] * tx + target->getDeriv()[1] * ty;

    //Dot product for normal vector
    float dpNorm1 = ball->getDeriv()[0] * nx + ball->getDeriv()[1] * ny;
    float dpNorm2 = target->getDeriv()[0] * nx + target->getDeriv()[1] * ny;

    //Conversion of momentum
    float m1 = (dpNorm1 * (ball->getStat()[0] - target->getStat()[0]) + 2.0f * target->getStat()[0] * dpNorm2) / (ball->getStat()[0] + target->getStat()[0]);
    float m2 = (dpNorm2 * (target->getStat()[0] - ball->getStat()[0]) + 2.0f * ball->getStat()[0] * dpNorm1) / (ball->getStat()[0] + target->getStat()[0]);

    //Update velocity of ball
    ball->updateDeriv(tx * dpTan1 + nx * m1, ty * dpTan1 + ny * m1, ball->getDeriv()[2], ball->getDeriv()[3]);
    target->updateDeriv(tx * dpTan2 + nx * m2, ty * dpTan2 + ny * m2, target->getDeriv()[2], target->getDeriv()[3]);
};