
def get_input():
  
  with open("day2.txt", "r") as tf:
    lines = tf.read().split("\n")
  return lines


def part1():
  rock_tie = 'A X'
  rock_loss = 'A Y'
  rock_won = 'A Z'
  
  paper_tie = 'B Y'
  paper_loss = 'B Z'
  paper_won = 'B X'

  scissor_tie = 'C Z'
  scissor_loss = 'C X'
  scissor_won = 'C Y'

  won = 6
  draw = 3
  lost = 0

  rock_score = 1
  paper_score = 2
  scissor_score = 3
  tournament = get_input()
  score = 0
  for game in tournament:
    if game == rock_tie:
      score += rock_score + draw
    elif game == rock_loss:
      score += paper_score + won
    elif game == rock_won:
      score += scissor_score + lost

    elif game == paper_tie:
      score += paper_score + draw
    elif game == paper_loss:
      score += scissor_score + won
    elif game == paper_won:
      score += rock_score + lost

    elif game == scissor_tie:
      score += scissor_score + draw
    elif game == scissor_loss:
      score += rock_score + won
    elif game == scissor_won:
      score += paper_score + lost
  print(score)

def part2():
  rock = 'A'
  paper = 'B'
  scissor = 'C'
  outcome_scores = {
    'A X':(3 +0),
    'A Y':(1 +3),
    'A Z':(2 +6),

    'B X':(1 +0),
    'B Y':(2 +3),
    'B Z':(3 +6),

    'C X':(2 +0),
    'C Y':(3 +3),
    'C Z':(1 +6),
  }
  tournament = get_input()
  score = 0
  for game in tournament:
    score += outcome_scores[game]
    
  print(score)


if __name__ == '__main__':
  part1()
  part2()