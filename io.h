#include <vector>
#include <string>
#include "Field.h"
#include "Objects.h"
#include "Physics.h"
#include <iostream>
#include <stdio.h>
#pragma once

namespace io {
	std::vector<Objects::Object> readObjects();

	std::vector<Field::Field> readBoundaries();

	std::string convert(Physics::Physics);

	void write(std::string);
};