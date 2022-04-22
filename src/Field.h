#pragma once
#include <vector>
#include <string>

namespace Field {
    class Field {
        float x1;
        float x2;
        float y1;
        float y2;
    public:
        void setPos(float, float, float, float);
        std::vector<float> getPos();
    };
};