#include "Field.h"
#include <vector>
#include <string>

void Field::Field::setPos(float nx1, float nx2, float ny1, float ny2) {
    x1 = nx1; x2 = nx2; y1 = ny1; y2 = ny2;
};

std::vector<float> Field::Field::getPos() {
    return std::vector<float> {x1, x2, y1, y2};
}