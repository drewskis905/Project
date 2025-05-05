#include <iostream>
#include <filesystem>
#include <vector>
#include <algorithm>
#include <string>
#include <unistd.h> // for fork(), exec(), and dup2()
#include <sys/wait.h>   // for waitpid()
#include <fcntl.h>  // for open()
#include <sstream>
namespace fs = std::filesystem;
int main() {
    // Copy your main from Homework 4 here, then continue the assignment.
    fs::path workingDir = "/";
    std::vector<std::string> history;
    std::istringstream commandInput;
    std::vector<std::string> arguments;
    std::string command;
    if (chdir(workingDir.c_str()) != 0) {
        return 1;
    }
    std::cout << "Welcome to AndrewShell\n" << std::endl;
    while (true) {
        std::cout << workingDir.string() << " $ " ;
        std::getline(std::cin, command);
        if (command == "exit") {
            break;
        }
        else if (command == "workingdir") {
            std::cout << "Working Directory: " << workingDir.string() << std::endl;
            history.push_back(std::move(command));
        }
        else if (command.substr(0,2) == "cd") {
            std::string x = command.substr(3);
            fs::path newPath;
            if (x[0] == '/') {
                newPath = fs::path(x);
            }
            else {
                newPath = workingDir / x;
                workingDir = fs::canonical(newPath);
            }
            do {
                newPath = fs::canonical(newPath);
                if (fs::exists(newPath)) {
                    workingDir = newPath;
                }
            }while (false);
            history.push_back(std::move(command));
            if (chdir(workingDir.c_str()) != 0) {
                return 1;
            }
        }
        else if (command == "list") {
            std::vector<fs::path> directories;
            std::vector<fs::path> files;
            for (const auto & entry : fs::directory_iterator(workingDir)) {
                if (entry.is_directory()) {
                    directories.push_back(entry.path());
                }
                else {
                    files.push_back(entry.path());
                }
            }
            std::sort(directories.begin(), directories.end());
            std::sort(files.begin(), files.end());
            for (const auto& directory : directories) {
                std::cout << directory.filename().string() << " (Directory)" << std::endl;
            }
            for (const auto& file : files) {
                std::cout << file.filename().string() << std::endl;
            }
            history.push_back(std::move(command));
        }
        else if (command == "history") {
            for (auto itr = history.end(); itr != history.begin(); ) {
                --itr;
                std::cout << *itr << "\n";
            }
        }
        else {
            size_t index = command.find(">");
            std::string copyCommand = command;
            std::string outFileName;
            if (index != std::string::npos) {
                outFileName = command.substr(index + 2);
                copyCommand = command.substr(0, command.find(">") - 1);
            }
            std::istringstream parse(copyCommand); //able to parse the command into its individual word
            std::string programPath;
            parse >> programPath; //for word in command will be the programs path
            std::vector<std::string> programArg; //list of arguments
            std::string arg;
            while (!parse.eof()) { //while the parse is not empty push the argument into the vector programArg
                parse >> arg;
                if (!arg.empty()) { //checks to see if the last thing in parse was pass into arg (because we don't want it)
                    programArg.push_back(arg);
                }
            }
            char** cargs = new char*[programArg.size() + 2];
            cargs[0] = programPath.data();
            for (size_t i = 0; i < programArg.size(); ++i) {
                cargs[i+1] = programArg[i].data();
            }
            cargs[programArg.size() + 1] = nullptr;
            int cid = fork();
            if (cid == 0) {
                int outputFile = open(outFileName.c_str(), O_WRONLY | O_CREAT | O_TRUNC, S_IRUSR | S_IWUSR);
                dup2(outputFile, STDOUT_FILENO);
                dup2(outputFile, STDERR_FILENO);
                execv(programPath.c_str(), cargs);
                std::cout << "Command could not be found" << std::endl;
                exit(1);
            }
            else {
                int statusCode;
                waitpid(cid, &statusCode, 0);
                if (statusCode != 0) {
                    std::cout << "Failed with code " << statusCode << std::endl;
                }
                delete[] cargs;
            }
            history.push_back(std::move(command));
        }
        std::cout << std::endl;
    }
    return 0;
}
