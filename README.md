# schedule-calc
Calculates a schedule for a league where no team plays another more than once.  Compatible with mid-season schedule changes.

## Issues
1. Can run into infinite loops.  
   * Rerun the program, if all settings are correct it will eventual find a compatiable schedule.  This will happen more often with larger numbers of teams.
2. Input is not checked.
   * Just follow the given limits and you should be fine.
3. Only works for even nunmbers of teams
   * Add one team and name it BYE or something else recognizable.
