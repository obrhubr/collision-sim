#include "Field.h"
#include <vector>
#include <string>

void Field::Field::setPos(float x1, float x2, float y1, float y2) {
    x1 = x1; x2 = x2; y1 = y1; y2 = y2;
};

std::vector<float> Field::Field::getPos() {
    return std::vector<float> {x1, x2, y1, y2};
}