#include <vector>
#include <string>
#include "Objects.h"

void Objects::Object::set(float m, float r, float b, float nposx, float nposy, float nxv, float nyv, float nxacc, float nyacc) {
    mass = m; radius = r; bounciness = b; posx = nposx; posy = nposy; xv = nxv; yv = nyv; xacc = nxacc; yacc = nyacc;
};

void Objects::Object::updatePos(float nPosx, float nPosy) {
    posx = nPosx;
    posy = nPosy;
};

void Objects::Object::updateDeriv(float nxv, float nyv, float nxacc, float nyacc) {
    xv = nxv; yv = nyv; xacc = nxacc; yacc = nyacc;
};

std::vector<float> Objects::Object::getPos() {
    return std::vector<float> {posx, posy};
};

std::vector<float> Objects::Object::getDeriv() {
    return std::vector<float> {xv, yv, xacc, yacc};
};

std::vector<float> Objects::Object::getStat() {
    return std::vector<float> {mass, radius, bounciness};
};