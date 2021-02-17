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
    };
};

void Physics::Physics::collisionCheck() {
    //Check collision between boundaries and objects
    
    //Check collision between object and object
    for (int i = 0; i < objectlist.size(); i++) {
        for (int j = 0; j < objectlist.size(); j++) {
            float r = objectlist[i].getStat()[1] + objectlist[j].getStat()[1];
            r *= r;
            float a = objectlist[i].getPos()[0] + objectlist[j].getPos()[0];
            float b = objectlist[i].getPos()[1] + objectlist[j].getPos()[1];
            float dist = a*a + b*b;
            if (r - dist <= 0) {
                bounce(i, j);
            };
        };
    };
};

void Physics::Physics::bounce(int i, int j) {
    //Handle collision between object and object

    //Handle collision between object and boundary
};