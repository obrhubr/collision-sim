#pragma once
#include "Field.h"
#include "Objects.h"
#include <vector>

namespace Physics {
    class Physics {
        std::vector<Objects::Object> objectlist;
        std::vector<Field::Field> boundarylist;
    public:
        void objects(std::vector<Objects::Object>);
        void boundary(std::vector<Field::Field>);
        std::vector<Objects::Object> getObjects();
        std::vector<Field::Field> getBoundaries();
        void update(float);
        void collisionCheck();
        void bounce(int, int);
    };
};