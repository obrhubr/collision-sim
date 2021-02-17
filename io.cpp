#include <vector>
#include <string>
#include "Field.h"
#include "Objects.h"
#include "Physics.h"
#include "io.h"
#include <iostream>
#include <stdio.h>

std::vector<Objects::Object> io::readObjects() {
    //Temp
    Objects::Object o1;
    Objects::Object o2;

    o1.set(10.0, 10.0, 1.0, 100.0, 100.0, 5.0, 5.0, 0.0, 0.0);
    o2.set(10.0, 10.0, 1.0, 100.0, 100.0, 5.0, 5.0, 0.0, 0.0);

    return std::vector<Objects::Object> { o1, o2 };
};

std::vector<Field::Field> io::readBoundaries() {
    //Temp
    return std::vector<Field::Field> {};
};

std::string io::convert(Physics::Physics physics) {
    std::vector<Objects::Object> objectlist = physics.getObjects();
    return std::to_string(objectlist[0].getPos()[0]);
}

void io::write(std::string content) {
    std::cout << content;
    return;
};