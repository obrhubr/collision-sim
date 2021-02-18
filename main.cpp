#include "Field.h"
#include "Objects.h"
#include "Physics.h"
#include "io.h"
#include <vector>
#include <string>

Physics::Physics setup(std::vector<Objects::Object> objectlist, std::vector<Field::Field> boundarylist) {
    Physics::Physics simulation;

    simulation.objects(objectlist);
    simulation.boundary(boundarylist);

    return simulation;
};

std::string runSimulation(int max, float dt, Physics::Physics physics) {
    int i = 0;
    while (i < max) {
        physics.update(dt);
        i++;
    };

    return io::convert(physics);
};

int main() {
    Physics::Physics physics = setup(io::readObjects(), io::readBoundaries());
    std::string content;

    content.append(runSimulation(5, 0.1, physics));

    io::write(content);
    
    return 1;
}