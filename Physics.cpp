#include "Field.h"
#include "Objects.h"
#include "Physics.h"
#include <vector>
#include <string>

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
    //Check for collision
    collisionCheck();
    //Update positions according to new velocity and acceleration
    for (int i = 0; i < objectlist.size(); i++) {
        objectlist[i].updatePos(objectlist[i].getPos()[0] + (objectlist[i].getDeriv()[0] * dt), objectlist[i].getPos()[1] + (objectlist[i].getDeriv()[1] * dt));
        objectlist[i].updateDeriv(objectlist[i].getDeriv()[0] + (objectlist[i].getDeriv()[2] * dt), objectlist[i].getDeriv()[1] + (objectlist[i].getDeriv()[3] * dt), objectlist[i].getDeriv()[2], objectlist[i].getDeriv()[3]);
    };
};

void Physics::Physics::collisionCheck() {
    //Check collision between boundaries and objects
    
    //Check collision between object and object
    for (int i = 0; i < objectlist.size(); i++) {
        for (int j = 0; j < objectlist.size(); j++) {
            if (i != j) {
                float r = objectlist[i].getStat()[1] + objectlist[j].getStat()[1];
                r *= r;
                float a = objectlist[i].getPos()[0] + objectlist[j].getPos()[0];
                float b = objectlist[i].getPos()[1] + objectlist[j].getPos()[1];
                float dist = a * a + b * b;
                if (r - dist <= 0) {
                    bounceBall(i, j);
                };
            };
        };
    };
};

void Physics::Physics::bounceBall(int i, int j) {
    //Handle collision between object and object

    //Get distance 
    float distance = sqrtf((objectlist[i].getPos()[0] - objectlist[j].getPos()[0]) * (objectlist[i].getPos()[0] - objectlist[j].getPos()[0]) + (objectlist[i].getPos()[1] - objectlist[j].getPos()[1]) * (objectlist[i].getPos()[1] - objectlist[j].getPos()[1]));

    //Get Normal vector
    float nx = (objectlist[j].getPos()[0] - objectlist[i].getPos()[0]) / distance;
    float ny = (objectlist[j].getPos()[1] - objectlist[i].getPos()[1]) / distance;

    //Tangent vector
    float tx = -ny;
    float ty = nx;

    //Dot product for Tangent
    float dpTan1 = objectlist[i].getDeriv()[0] * tx + objectlist[i].getDeriv()[1] * ty;
    float dpTan2 = objectlist[j].getDeriv()[0] * tx + objectlist[j].getDeriv()[1] * ty;

    //Dot product for normal vector
    float dpNorm1 = objectlist[i].getDeriv()[0] * nx + objectlist[i].getDeriv()[1] * ny;
    float dpNorm2 = objectlist[j].getDeriv()[0] * nx + objectlist[j].getDeriv()[1] * ny;

    //Conversation of momentum
    float m1 = (dpNorm1 * (objectlist[i].getStat()[0] - objectlist[j].getStat()[0]) + 2.0f * objectlist[j].getStat()[0] * dpNorm2) / (objectlist[i].getStat()[0] + objectlist[j].getStat()[0]);
    float m2 = (dpNorm2 * (objectlist[j].getStat()[0] - objectlist[i].getStat()[0]) + 2.0f * objectlist[i].getStat()[0] * dpNorm2) / (objectlist[i].getStat()[0] + objectlist[j].getStat()[0]);

    //Update velocity of ball
    objectlist[i].updateDeriv(tx * dpTan1 + nx * m1, ty * dpTan1 + ny * m1, objectlist[i].getDeriv()[2], objectlist[i].getDeriv()[3]);
    objectlist[j].updateDeriv(tx * dpTan2 + nx * m1, ty * dpTan2 + ny * m1, objectlist[j].getDeriv()[2], objectlist[j].getDeriv()[3]);
};

void Physics::Physics::bounceWall(int i, int j) {

}