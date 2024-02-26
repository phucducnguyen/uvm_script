The Purpose of this script is to generate the UVM template.
There are 9 main UVM Phases.

                     _____________         _ 
                    /    BUILD    \         |
                    \_____________/         |
                          ||                |
                     _____\/______          |
                    /   CONNECT   \         |----  Build Time.  
                    \_____________/         |
                          ||                |
                 _________\/_________       |
                / END_OF_ELABORATION \      |
                \____________________/     _|
                          ||             
         _       _________\/__________
        |       / START OF SIMULATION \ 
    RUN |       \_____________________/
    TIME|                 ||
        |            _____\/______      _
        |           /    RUN      \      |  ONE AND ONLY TASK FROM ALL THE PHASES. CAN TAKE DELAYS.
        |_          \_____________/     _|  ALL OTHER UVM_PHASES ARE FUNCTIONS.
                          ||
                     _____\/______
                    /   EXTRACT   \        _
                    \_____________/         |
                          ||                |
                     _____\/______          |
                    /    CHECK    \         |
                    \_____________/         |
                          ||                |----- Clean up 
                     _____\/______          |
                    /   REPORT    \         |
                    \_____________/         |
                          ||                |
                     _____\/______          |
                    /    FINAL    \        _|
                    \_____________/ 


If you'd like to learn more on Phases, Visit "http://www.verificationguide.com/p/uvm-phases.html"
