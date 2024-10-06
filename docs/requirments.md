# Project Requirements and Goals

Project goals: To create a tool which can assist with learning how to type on a new keyboard and a new layout.  
The end vision for this tool is for it to show chracters, words, phrases, or whole paragraphs on a screen depending on the mode chosen. The user will then attempt to type back what the tool has shown, as quickly and accurately as they can. The tool will measure the time taken by the user for each unit shown, track how much they got correct, and show the result on screen. Additional metrics may be added if any are thought of.   

The project will be developed in multiple phases, though an end-to-end skeleton will be built asap, hopefully by the end of the second phase.

## Requirements
### Phase 1
Functional requirements: To begin, the first goal should be to build the simplest version possible. Therefore, the initial development of the tool will be entirely terminal based, with no front end, and only one of the desired modes implemented. Showing random characters is likely the easiest and so will be what is shown.  

Non-Functional Requirements: The tool will print out a word in the terminal, and ask for user input. At this point it will start a timer. The user will type back the word shown by the tool, and will need press enter to return the word. The tool will stop the timer and repeat the cycle, 3 times to begin with.

Tool & Tech:  
The backend will be written in Python, this is the only consideration needed for this first phase.

Steps
1. ~~Session starts~~
2. ~~Random characters generated~~
3. ~~Print generated characters out to terminal~~
4. ~~Start timer~~
5. ~~User input word~~
6. ~~Stop timer~~
7. ~~Store output characters, user input, time~~
8. ~~Repeat 10 times~~
9. ~~Finish session~~
10. ~~Calculate accuracy and time~~
11. ~~Output results~~
#### Phase 1 Complete.

### Phase 2
Functional requirements: Now that a simple backend has been created, need to create a simple frontend to hook it up to. The frontend needs to have a start button, and show the results in the middle of the screen and it will be black and white. The round's text to type will show up in the middle of the screen, and the user input will have a text box.

Non-Functional requirements: The frontend will use either tkinter or pygame, quick exploration will be done on both to choose the appropriate one.

Steps:
1. Find out enough to choose between pygame or tkinter.
2. Create quick diagram of basic layout.
3. Find functions and classes that need to be used or made to get basic layout up.
4. Code basic wireframe.
5. Find out enough to try and integrate the backend and frontend.
6. Try.
