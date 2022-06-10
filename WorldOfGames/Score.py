from Utils import SCORES_FILE_NAME
import Utils
import os.path


def add_score(difficulty):
    current_score = get_current_score()
    if(current_score == ''):
        current_score = 0
    current_score_number =int(current_score)
    difficulty_number =int(difficulty)
    points_of_winning = ( difficulty_number* 3) +5
    updated_score =  current_score_number + points_of_winning
    set_score(updated_score)


def set_score(score):
        f= open(SCORES_FILE_NAME,"w")
        f.write(str(score))
        f.close()


def get_current_score():
    try:
        isFileExist = os.path.exists(SCORES_FILE_NAME)
        if  isFileExist:
            f= open(SCORES_FILE_NAME,"r")
            scores = f.read()
            f.close()
            return scores
        else:
          return 0
    except :
        return Utils.BAD_RETURN_CODE



