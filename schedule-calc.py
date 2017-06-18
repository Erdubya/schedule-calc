from random import choice

"""
:author: Erik Wilson
:email: erikwilson@outlook.com

This module will generate a schedule for a league, ensuring that no team plays
another more than once.  

There is an issue where it can hang in an infinite loop.  Should this occur, 
rerun the program until you receive a result.  It will occur more with larger 
numbers of teams
"""


class Team:
    """
    Team encapsulates a team, including its number, and what team it has yet to
    play
    """

    team_cnt = 0

    def __init__(self):
        """
        Construct a new Team
        """
        Team.team_cnt += 1

        self.team_num = Team.team_cnt
        self.unplayed = {i + 1 for i in range(tot_teams)}

    def __str__(self):
        return str(self.get_team_num())

    def get_team_num(self):
        """
        Returns the team's number
        :return: The team's number
        """
        return self.team_num

    def play_team(self, team_num):
        """
        Mark the given team as played

        :param team_num: The team to play
        :return: Nothing
        """
        if self.check_played(team_num):
            self.unplayed.remove(team_num)
        else:
            print("already played!")

    def check_played(self, team_num):
        """
        Check if a team has been played
        :param team_num: The team to check
        :return: True if not played, false if played
        """
        if team_num in self.unplayed:
            return True
        else:
            return False


def diff(a, b):
    """
    Returns the set difference of two iterables
    :param a: The minuend
    :param b: The subtrahend
    :return: The resulting set
    """
    return {item for item in a if item not in b}


def get_num_teams():
    """
    Get the total number of teams from the user, setting bye if necessary
    :return: The user-input total number of teams
    """
    num_teams = 0
    while num_teams <= 0:
        num_teams = int(input("Enter number of teams (x > 0): "))
        if num_teams > 0 and num_teams % 2 is 1:
            # Set BYE team if odd number of teams
            num_teams += 1
            print("Team", num_teams, "is a BYE")
    return num_teams


def get_season_weeks():
    """
    Gets the total number of weeks in the season from the user
    :return: The user input number of weeks
    """
    num_weeks = -1
    while num_weeks < 0:
        num_weeks = int(input("Total weeks of play (0 <= x < "
                              + str(tot_teams) + "): "))
    return num_weeks


def get_done_weeks():
    """
    Gets the number of weeks already played from the user.
    :return: The user-entered number of weeks played
    """
    done = -1
    while done < 0:
        done = int(input("Weeks already played (0 <= x <= "
                         + str(tot_weeks) + "):"))
    return done


def get_week_matchups():
    """
    Gets a set of matchups from a previously played week
    :return: None
    """
    weeks.append([])
    print("Week %d:" % len(weeks))

    for j in range(0, int(tot_teams / 2)):
        print("matchup %d:" % (j + 1))
        team1 = int(input("Enter first team: "))
        team2 = int(input("Enter second team: "))
        print("\n")

        teams[team1 - 1].play_team(team2 - 1)
        teams[team2 - 1].play_team(team1 - 1)

        temp = (team1, team2)
        weeks[i].append(temp)

    return None


def check_week_played(a_team, a_week):
    """
    Checks if a team has played in a given week
    :param a_team: The team to check
    :param a_week: The week to check for the team
    :return: True if the team is found, false otherwise
    """
    for x in a_week:
        if a_team in x:
            return True
    return False

tot_teams = get_num_teams()
tot_weeks = get_season_weeks()
done_weeks = get_done_weeks()

# Initialize lists
teams = [Team() for i in range(tot_teams)]
weeks = []

# Get info for previously played weeks
if done_weeks > 0:
    for i in range(done_weeks):
        get_week_matchups()

# For each unplayed week
while len(weeks) is not tot_weeks:
    # Add a new week
    week = len(weeks)
    weeks.append([])

    # For each team
    for team in range(1, tot_teams+1):
        # Check if already played this week
        played = check_week_played(team, weeks[week])

        #  If not, get opponent
        if not played:
            # Check each possible opponent
            while True:
                # Get a set of teams to play
                ls_week = {i for x in weeks[week] for i in x}
                ls_unplayed = teams[team - 1].unplayed
                ls_choice = diff(ls_unplayed, ls_week)

                # If there are teams available, pick one to play
                if len(ls_choice) is not 0:
                    vs = choice(tuple(ls_choice))
                else:
                    break

                # Check if possible opponent has played this week
                isin = check_week_played(vs, weeks[week])

                # redo the week if there is not an option for the team
                # print(vs)
                # print(isin)

                # If they have not played this week, add the match
                if not isin:
                    match = (team, vs)
                    weeks[week].append(match)
                    break

    # Make sure the week has enough matches
    if len(weeks[week]) is not int((tot_teams / 2)):
        #  If not, redo the week
        weeks.pop()
    else:
        # otherwise, mark each match as played
        for match in weeks[week]:
            teams[match[0] - 1].play_team(match[1])
            teams[match[1] - 1].play_team(match[0])

# Print the resulting schedule
for x in weeks:
    s = ""
    for m in x:
        s = s + "{0:3} v {1:2},".format(m[0], m[1])
    print(s)

