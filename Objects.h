#pragma once
#include <vector>
#include <string>

namespace Objects {
    class Object {
        float mass;
        float radius;
        float bounciness;
        float posx;
        float posy;
        float xv;
        float yv;
        float xacc;
        float yacc;
    public:
        void set(float, float, float, float, float, float, float, float, float);
        void updatePos(float, float);
        void updateDeriv(float, float, float, float);
        std::vector<float> getPos();
        std::vector<float> getDeriv();
        std::vector<float> getStat();
    };
};
 
