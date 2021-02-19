#include <vector>
#include <string>
#include "Field.h"
#include "Objects.h"
#include "Physics.h"
#include "io.h"
#include <iostream>
#include <stdio.h>
#include <fstream>
#include <sstream>

std::vector<Objects::Object> io::readObjects() {
    std::vector<Objects::Object> objects;

    std::ifstream infile("data.setup");
    for (std::string line; getline(infile, line); ) {
        if (line.at(0) == 'B') {
            
        }
        else if (line.at(0) == 'O') {
            std::stringstream ss(line);
            std::vector<float> objData;
            int counter = 0;
            while (ss.good()) {
                std::string substr;
                std::getline(ss, substr, ','); //get first string delimited by comma
                if (counter != 0) {
                    objData.push_back(std::stof(substr));
                };
                counter++;
            };
            Objects::Object tempObj;
            tempObj.set(objData[0], objData[1], objData[8], objData[2], objData[3], objData[4], objData[5], objData[6], objData[7]);
            objects.push_back(tempObj);
        }
        else {

        };
    };

    return objects;
};

std::vector<Field::Field> io::readBoundaries() {
    std::vector<Field::Field> boundaries;

    std::ifstream infile("data.setup");
    for (std::string line; getline(infile, line); ) {
        if (line.at(0) == 'B') {
            std::stringstream ss(line);
            std::vector<int> objData;
            int counter = 0;
            while (ss.good()) {
                std::string substr;
                std::getline(ss, substr, ','); //get first string delimited by comma
                if (counter != 0) {
                    objData.push_back(std::stoi(substr));
                };
                counter++;
            };
            Field::Field tempObj;
            tempObj.setPos(objData[0], objData[1], objData[2], objData[3]);
            boundaries.push_back(tempObj);
        };
    };

    return boundaries;
};

float io::readSigma() {
    //std::ifstream infile("data.setup");
    //int counter = 0;
    //for (std::string line; getline(infile, line); ) {
    //    if (counter == 0) {
    //        std::stringstream ss(line);
    //        while (ss.good()) {
    //            std::string substr;
    //            std::getline(ss, substr, ','); //get first string delimited by comma
    //            return std::stof(substr);
    //        };
    //    };
    //    counter++;
    //};
    return 0.1;
};

int io::readTotalTime() {
    //std::ifstream infile("data.setup");
    //int counter = 0;
    //for (std::string line; getline(infile, line); ) {
    //    if (counter == 0) {
    //        std::stringstream ss(line);
    //        int counter2 = 0;
    //        while (ss.good()) {
    //            std::string substr;
    //            std::getline(ss, substr, ','); //get first string delimited by comma
    //            if (counter == 1) {
    //                return std::stoi(substr);
    //            };
    //            counter++;
    //        };
    //    };
    //    counter++;
    //};
    return 100;
};

std::string io::convert(Physics::Physics physics) {
    std::vector<Objects::Object> objectlist = physics.getObjects();
    std::string content;
    for (int i = 0; i < objectlist.size(); i++) {
        content.append(std::to_string((int)objectlist[i].getPos()[0]));
        content.append(",");
        content.append(std::to_string((int)objectlist[i].getPos()[1]));
        content.append(",");
    };
    content.append("\n");
    return content;
};

void io::write(std::string content) {
    std::cout << content;
    std::ofstream myfile;
    myfile.open("output.data");
    myfile << content;
    myfile.close();
    return;
};