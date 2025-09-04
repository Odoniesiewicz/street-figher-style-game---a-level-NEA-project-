import pygame
import time
import random
import ast
from sys import exit
import os
##from menu import *
pygame.init()
pygame.mixer.init()
available_characters=['1','2','3','4','5','6','7','8','9','0','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
SCREEN_WIDTH=1000
SCREEN_HEIGHT=500
gravity=1.9
LONG_RANGE=500
SHORT_RANGE=155
DIFFICULTY_SELECT="hard"
Attack_cooldown=400
walk_cooldown=250
skillpoint_cooldown =25
game_started=False
start_screen=True
last_error_time=0
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('FIGHT CLUB')
##blurred surface for pause menu
blurred_screen=pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT),pygame.SRCALPHA)
##running=True
##background

##base directories
IMAGES_FOLDER = os.path.join("IMAGES", "BACKGROUNDS")
SPRITES_FOLDER=os.path.join("IMAGES", "SPRITES")
BUTTONS_OTHER_FOLDER=os.path.join("IMAGES", "BUTTONS+OTHER")
# load + scale the backgrounds
bg_1 = pygame.image.load(os.path.join(IMAGES_FOLDER, 'bg1.gif'))
bg_1 = pygame.transform.scale(bg_1, (SCREEN_WIDTH, SCREEN_HEIGHT))
bg_2 = pygame.image.load(os.path.join(IMAGES_FOLDER, 'bg2.gif'))
bg_2 = pygame.transform.scale(bg_2, (SCREEN_WIDTH, SCREEN_HEIGHT))
bg_3 = pygame.image.load(os.path.join(IMAGES_FOLDER, 'bg3.jpeg'))
bg_3 = pygame.transform.scale(bg_3, (SCREEN_WIDTH, SCREEN_HEIGHT))
bg_4 = pygame.image.load(os.path.join(IMAGES_FOLDER, 'bg4.png'))
bg_4 = pygame.transform.scale(bg_4, (SCREEN_WIDTH, SCREEN_HEIGHT))
backgrounds = [bg_1, bg_2, bg_3]
# intro backgrounds
intro_bg = pygame.image.load(os.path.join(IMAGES_FOLDER, 'intro_bg.png'))
intro_bg = pygame.transform.scale(intro_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
intro_bg2 = pygame.image.load(os.path.join(IMAGES_FOLDER, 'intro_bg2.png'))
intro_bg2 = pygame.transform.scale(intro_bg2, (SCREEN_WIDTH, SCREEN_HEIGHT))
champion_img=pygame.image.load(os.path.join(BUTTONS_OTHER_FOLDER,'champion.png'))
background1_img=pygame.transform.scale(bg_1,(180,180))
background2_img=pygame.transform.scale(bg_2,(180,180))
background3_img=pygame.transform.scale(bg_3,(180,180))
background4_img=pygame.transform.scale(bg_4,(180,180))
championbg_img=pygame.image.load(os.path.join(IMAGES_FOLDER,'championbg.png'))
championbg_img=pygame.transform.scale(championbg_img,(SCREEN_WIDTH,SCREEN_HEIGHT))

#MENU
#BUTTON IMAGES
start_img = pygame.image.load(os.path.join(BUTTONS_OTHER_FOLDER, 'START.png'))
startgame_img = pygame.image.load(os.path.join(BUTTONS_OTHER_FOLDER, 'START GAME.png'))
quit_img = pygame.image.load(os.path.join(BUTTONS_OTHER_FOLDER, 'QUIT.png'))
restart_img = pygame.image.load(os.path.join(BUTTONS_OTHER_FOLDER, 'RESTART.png'))
loadgame_img = pygame.image.load(os.path.join(BUTTONS_OTHER_FOLDER, 'LOAD GAME.png'))
newgame_img = pygame.image.load(os.path.join(BUTTONS_OTHER_FOLDER, 'NEW GAME.png'))
credits_img = pygame.image.load(os.path.join(BUTTONS_OTHER_FOLDER, 'CREDITS.png'))
shop_img = pygame.image.load(os.path.join(BUTTONS_OTHER_FOLDER, 'SHOP.png'))
controls_img = pygame.image.load(os.path.join(BUTTONS_OTHER_FOLDER, 'CONTROLS.png'))
back_img = pygame.image.load(os.path.join(BUTTONS_OTHER_FOLDER, 'BACK.png'))
vsmode_img = pygame.image.load(os.path.join(BUTTONS_OTHER_FOLDER, 'vs mode.png'))
buy_img = pygame.image.load(os.path.join(BUTTONS_OTHER_FOLDER, 'buy.png'))
textbox_img = pygame.image.load(os.path.join(BUTTONS_OTHER_FOLDER, 'textbox.png'))
characterselect_img = pygame.image.load(os.path.join(BUTTONS_OTHER_FOLDER, 'characterselect.png'))
balrogselect_img = pygame.image.load(os.path.join(BUTTONS_OTHER_FOLDER, 'balrogselect.png'))
winnerquit_img = pygame.image.load(os.path.join(BUTTONS_OTHER_FOLDER, 'quit_gold.png'))
nextlevel_img = pygame.image.load(os.path.join(BUTTONS_OTHER_FOLDER, 'next level.png'))
defendtitle_img = pygame.image.load(os.path.join(BUTTONS_OTHER_FOLDER, 'defend title.png'))
whitebox_img = pygame.image.load(os.path.join(BUTTONS_OTHER_FOLDER, 'whitebox.png'))
checkedbox_img = pygame.image.load(os.path.join(BUTTONS_OTHER_FOLDER, 'checkedbox.png'))

# OTHER IMAGES
title_img = pygame.image.load(os.path.join(BUTTONS_OTHER_FOLDER, 'TITLE_3.png'))
winner_img = pygame.image.load(os.path.join(BUTTONS_OTHER_FOLDER, 'WINNER.png'))
defeat_img = pygame.image.load(os.path.join(BUTTONS_OTHER_FOLDER, 'DEFEAT.png'))
enteryoursaved_img = pygame.image.load(os.path.join(BUTTONS_OTHER_FOLDER, 'ENTER YOUR SAVED.png'))
enteryournew_img = pygame.image.load(os.path.join(BUTTONS_OTHER_FOLDER, 'ENTER YOUR NEW.png'))
gamename_img = pygame.image.load(os.path.join(BUTTONS_OTHER_FOLDER, 'GAME NAME.png'))
skillpoints_img = pygame.image.load(os.path.join(BUTTONS_OTHER_FOLDER, 'SKILL POINTS.png'))
ryuname_img = pygame.image.load(os.path.join(BUTTONS_OTHER_FOLDER, 'RYU_name.png'))
balrogname_img = pygame.image.load(os.path.join(BUTTONS_OTHER_FOLDER, 'BALROG_name.png'))
controllist_img = pygame.image.load(os.path.join(BUTTONS_OTHER_FOLDER, 'CONTROLs_list.png'))
credit_img = pygame.image.load(os.path.join(BUTTONS_OTHER_FOLDER, 'credit.png'))
specialmovedescription1_img = pygame.image.load(os.path.join(BUTTONS_OTHER_FOLDER, 'specialmovedescription1.png'))
specialmovedescription2_img = pygame.image.load(os.path.join(BUTTONS_OTHER_FOLDER, 'specialmovedescription2.png'))
specialmovedescription3_img = pygame.image.load(os.path.join(BUTTONS_OTHER_FOLDER, 'specialmovedescription3.png'))
error_img = pygame.image.load(os.path.join(BUTTONS_OTHER_FOLDER, 'error.png'))
coin_img = pygame.image.load(os.path.join(BUTTONS_OTHER_FOLDER, 'coin.png'))
chooseyourcharacter_img = pygame.image.load(os.path.join(BUTTONS_OTHER_FOLDER, 'chooseyourcharacter.png'))
characterselect2_img = pygame.image.load(os.path.join(BUTTONS_OTHER_FOLDER, 'characterselect2.png'))
ryupreview_img = pygame.image.load(os.path.join(BUTTONS_OTHER_FOLDER, 'ryupreview.png'))
balrogpreview_img = pygame.image.load(os.path.join(BUTTONS_OTHER_FOLDER, 'balrogpreview.png'))
selectlocation_img = pygame.image.load(os.path.join(BUTTONS_OTHER_FOLDER, 'select location.png'))
belt_img = pygame.image.load(os.path.join(BUTTONS_OTHER_FOLDER, 'belt.png'))
player1_img = pygame.image.load(os.path.join(BUTTONS_OTHER_FOLDER, 'player1.png'))
player2_img = pygame.image.load(os.path.join(BUTTONS_OTHER_FOLDER, 'player2.png'))
##sounds
music={'menu':'AUDIO/menu music.mp3','maingame':'AUDIO/maingame.mp3','winner':'AUDIO/winner.mp3','defeat':'AUDIO/defeat.mp3','champion':'AUDIO/champion.mp3'}
hit=pygame.mixer.Sound('AUDIO/punchlanded.wav')
miss=pygame.mixer.Sound('AUDIO/miss.mp3')
click=pygame.mixer.Sound('AUDIO/select.wav')
##balrog sprites
##user
balrog_standing = [pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogstanding1.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogstanding2.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogstanding3.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogstanding4.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogstanding1.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogstanding2.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogstanding3.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogstanding4.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogstanding1.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogstanding2.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogstanding3.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogstanding4.png'))]

balrog_walking = [pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogwalking1.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogwalking2.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogwalking3.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogwalking4.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogwalking1.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogwalking2.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogwalking3.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogwalking4.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogwalking1.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogwalking2.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogwalking3.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogwalking4.png'))]

balrog_crouching = [pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogcrouching1.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogcrouching2.png'))]

balrog_jumping = [pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogjump1.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogjump2.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogjump3.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogjump4.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogjump5.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogjump6.png'))]

# Attacks
balrog_L_attack = [pygame.image.load(os.path.join(SPRITES_FOLDER, 'balroglpunch1.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'balroglpunch2.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'balroglpunch3.png'))]

balrog_R_attack = [pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogrpunch1.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogrpunch2.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogrpunch3.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogrpunch4.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogrpunch5.png'))]

balrog_Attack_3 = [pygame.image.load(os.path.join(SPRITES_FOLDER, 'balroguppercut1.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'balroguppercut2.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'balroguppercut3.png'))]

# Reactions
balrog_head_reaction = [pygame.image.load(os.path.join(SPRITES_FOLDER, 'balroghit1.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'balroghit2.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'balroghit3.png'))]

balrog_body_reaction = [pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogbodyhit1.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogbodyhit2.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogbodyhit3.png'))]

balrog_knockout = [pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogknockout1.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogknockout2.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogknockout3.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogknockout4.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogknockout5.png'))]

# Celebrations
balrog_celebration1 = [pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogcelebration1.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogcelebration2.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogcelebration3.png'))]

# Flipped (for opponent)
balrog_standing_flip = [pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogstanding1.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogstanding2.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogstanding3.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogstanding4.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogstanding1.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogstanding2.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogstanding3.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogstanding4.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogstanding1.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogstanding2.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogstanding3.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogstanding4.png')), True, False)]

balrog_walking_flip = [pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogwalking1.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogwalking2.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogwalking3.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogwalking4.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogwalking1.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogwalking2.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogwalking3.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogwalking4.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogwalking1.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogwalking2.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogwalking3.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogwalking4.png')), True, False)]

balrog_crouching_flip = [pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogcrouching1.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogcrouching2.png')), True, False)]

balrog_jumping_flip = [pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogjump1.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogjump2.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogjump3.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogjump4.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogjump5.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogjump6.png')), True, False)]

# Attacks (Flipped)
balrog_L_attack_flip = [pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balroglpunch1.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balroglpunch2.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balroglpunch3.png')), True, False)]

balrog_R_attack_flip = [pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogrpunch1.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogrpunch2.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogrpunch3.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogrpunch4.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogrpunch5.png')), True, False)]

balrog_Attack_3_flip = [pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balroguppercut1.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balroguppercut2.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balroguppercut3.png')), True, False)]

##Reactions flipped
balrog_head_reaction_flip = [pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balroghit1.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balroghit2.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balroghit3.png')), True, False)]

balrog_body_reaction_flip = [pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogbodyhit1.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogbodyhit2.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogbodyhit3.png')), True, False)]

balrog_knockout_flip = [pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogknockout1.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogknockout2.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogknockout3.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogknockout4.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'balrogknockout5.png')), True, False)]

##ryu sprites
ryu_standing = [pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryustanding1.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryustanding2.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryustanding3.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryustanding4.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryustanding5.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryustanding1.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryustanding2.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryustanding3.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryustanding4.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryustanding5.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryustanding1.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryustanding2.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryustanding3.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryustanding4.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryustanding5.png'))]

ryu_walking = [pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuwalking1.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuwalking2.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuwalking3.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuwalking4.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuwalking1.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuwalking2.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuwalking3.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuwalking4.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuwalking1.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuwalking2.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuwalking3.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuwalking4.png'))]

ryu_crouching = [pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryucrouching1.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryucrouching2.png'))]

ryu_jumping = [pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryujump1.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryujump2.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryujump3.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryujump4.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryujump5.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryujump6.png'))]

# Attacks
ryu_L_kick = [pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryulkick1.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryulkick2.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryulkick3.png'))]

ryu_R_kick = [pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryurkick1.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryurkick2.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryurkick3.png'))]

ryu_Axe = [pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuaxe1.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuaxe2.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuaxe3.png'))]

ryu_360 = [pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryu3601.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryu3602.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryu3603.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryu3604.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryu3605.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryu3606.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryu3607.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryu3608.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryu3609.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryu36010.png'))]

# Reactions
ryu_head_reaction = [pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuhit1.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuhit2.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuhit3.png'))]

ryu_body_reaction = [pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryubodyhit1.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryubodyhit2.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryubodyhit3.png'))]

ryu_knockout = [pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuknockout1.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuknockout2.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuknockout3.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuknockout4.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuknockout5.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuknockout6.png')),
    pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuknockout7.png'))]

# Opponent (flipped)
ryu_standing_flip = [pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryustanding1.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryustanding2.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryustanding3.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryustanding4.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryustanding1.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryustanding2.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryustanding3.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryustanding4.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryustanding1.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryustanding2.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryustanding3.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryustanding4.png')), True, False)]

ryu_walking_flip = [pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuwalking1.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuwalking2.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuwalking3.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuwalking4.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuwalking1.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuwalking2.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuwalking3.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuwalking4.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuwalking1.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuwalking2.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuwalking3.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuwalking4.png')), True, False)]

ryu_crouching_flip = [pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryucrouching1.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryucrouching2.png')), True, False)]

ryu_jumping_flip = [pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryujump1.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryujump2.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryujump3.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryujump4.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryujump5.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryujump6.png')), True, False)]

## attacks (flipped)
ryu_L_kick_flip = [pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryulkick1.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryulkick2.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryulkick3.png')), True, False)]

ryu_R_kick_flip = [pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryurkick1.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryurkick2.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryurkick3.png')), True, False)]

ryu_Axe_flip = [pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuaxe1.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuaxe2.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuaxe3.png')), True, False)]

ryu_360_flip = [pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryu3601.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryu3602.png')), True,False)]

# reactions (flipped)
ryu_head_reaction_flip = [pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuhit1.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuhit2.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuhit3.png')), True, False)]

ryu_body_reaction_flip = [pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryubodyhit1.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryubodyhit2.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryubodyhit3.png')), True, False)]

ryu_knockout_flip = [pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuknockout1.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuknockout2.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuknockout3.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuknockout4.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuknockout5.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuknockout6.png')), True, False),
    pygame.transform.flip(pygame.image.load(os.path.join(SPRITES_FOLDER, 'ryuknockout7.png')), True, False)]
## character class
class character(object):
    def __init__(self,x,y,width,height,health,name,style,has_skillmove,left_right,target):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.name=name
        self.style=style
        self.has_skillmove=has_skillmove
        self.vel=5
        self.y_vel=0
        self.Left=False
        self.Right=False
        self.Crouch=False
        self.Jump=False
        self.L_attack=False
        self.R_attack=False
        self.Attack_3=False
        self.Attack_4=False
        self.Attacking=False
        self.Head_hit=False
        self.Body_hit=False
        self.Knockout=False
        self.Dead=False
        self.walkCount=0
        self.on_ground=True
        self.jumpCount=0
        self.attack_Count=0
        self.left_right=left_right
        self.target=target
        self.health=health
        self.Block=False
        self.last_attack_time=0
        self.last_movement_time=0
        self.last_collision_time=0
        self.outline_rect = balrog_standing[0].get_rect(topleft=(self.x, self.y))
        self.L_attack_rect = balrog_L_attack[1].get_rect(topleft=(self.x, self.y))
        self.R_attack_rect = balrog_R_attack[2].get_rect(topleft=(self.x, self.y))
        self.uppercut_rect = balrog_Attack_3[1].get_rect(topleft=(self.x, self.y))
        self.L_kick_rect = ryu_L_kick[2].get_rect(topleft=(self.x, self.y))
        self.R_kick_rect = ryu_R_kick[2].get_rect(topleft=(self.x, self.y))
        self.axe_rect = ryu_Axe[2].get_rect(topleft=(self.x, self.y))
        self.Attack4_rect= ryu_360[4].get_rect(topleft=(self.x, self.y))
        self.skillpoints=0
        self.lastskillpointupdate=0
        self.skillmove_available=False
        self.skillmove=None
## movement functions
    def left(self):
        self.x-=self.vel
        self.Left=True
        
    def right(self):
        self.x+=self.vel
        self.Right=True
        
    def jump(self):
        self.y_vel=13
        self.Jump=True
        self.on_ground=False
        self.jumpCount=0
    def crouch(self):
        self.Crouch=True
        self.Block=True
        
    def l_attack(self):        
        self.L_attack=True
        self.Attacking=True
        user.sound_played=False
        self.walkCount=1
    def r_attack(self):        
        self.R_attack=True
        self.Attacking=True
        user.sound_played=False
        self.walkCount=1        
    def attack_3(self):
        self.Attack_3=True
        self.Attacking=True
        user.sound_played=False
        self.walkCount=1
    def attack_4(self):
        self.Attack_4=True
        self.Attacking=True
        user.sound_played=False
        self.walkCount=1
    def knockout(self):
        self.Knockout=True
        self.walkCount=1
## update method for animations
    def update(self,current_time):
        #prevent player from walking off screen    
        if  not self.x-self.vel>=0:
                self.x=1
        if not self.x+self.width<SCREEN_WIDTH:
                self.x=SCREEN_WIDTH-self.width
        if self.walkCount+1==36:
                self.walkCount=0
        if self.Right and self.on_ground:
               self.walkCount+=1
               self.Right=False
##goes through all the snimation steps for the knockout then when reaches the last one dead is set to true , and the last animation frame remains
        if self.Knockout:
            self.walkCount+=1
            self.attack_Count+=1                        
            if self.attack_Count==7:
                print('dead')
                self.Dead=True
                self.Knockout=False
                self.Attacking=False
        elif self.Left and self.on_ground:
               self.walkCount+=1
               self.Left=False
        elif self.Crouch and self.on_ground:
                self.walkCount+=1
                self.Crouch=False
                self.Block=False
        #jumping mechanics
        elif self.Jump:
            if self.jumpCount<6:
                self. jumpCount+=1
            self.y-=self.y_vel                
            self.y_vel-=gravity
            self.walkCount+=1
           
            if self.y>=150:
                self.y=150
                self.on_ground=True
                self.Jump=False
        elif self.L_attack:               
                self.walkCount+=1
                self.attack_Count+=1
                if self.attack_Count==4:
                    self.L_attack=False
                    self.Attacking=False
                    self.attack_Count=0
                    
        elif self.R_attack:               
                self.walkCount+=1
                self.attack_Count+=1
                #when attack reaches final animation frame, set to false
                if self.attack_Count==5:
                    self.R_attack=False
                    self.Attacking=False
                    self.attack_Count=0
        elif self.Attack_3:               
            self.walkCount+=1
            self.attack_Count+=1
            if self.attack_Count==4:
                self.Attack_3=False
                self.Attacking=False
                self.attack_Count=0
        elif self.Attack_4:
            self.walkCount+=1
            self.attack_Count+=1
            if self.attack_Count==10:
                self.Attack_4=False
                self.Attacking=False
                self.attack_Count=0
        elif self.Head_hit:
            self.walkCount+=1
            self.attack_Count+=1
            if self.attack_Count==3:
                self.Head_hit=False
                self.attack_Count=0
        elif self.Body_hit:
            self.walkCount+=1
            self.attack_Count+=1
            if self.attack_Count==3:
                self.Body_hit=False
                self.attack_Count=0
##      collision checking method , check if rectagles collide while player attacks, also check for block
    def attack(self,target,current_time):
        #collision rect for balrog1
        balroglpunch_rect=pygame.Rect(balrog.x-40,balrog.y,*self.L_attack_rect.size)
        balrogrpunch_rect=pygame.Rect(balrog.x-40,balrog.y,*self.R_attack_rect.size)
        balroguppercut_rect=pygame.Rect(balrog.x-40,balrog.y,*self.uppercut_rect.size)

        #collision rect for ryu1
        ryulkick_rect=pygame.Rect(ryu.x-40,ryu.y,*self.L_kick_rect.size)
        ryurkick_rect=pygame.Rect(ryu.x-40,ryu.y,*self.R_kick_rect.size)
        ryuaxe_rect=pygame.Rect(ryu.x-40,ryu.y,*self.axe_rect.size)
        ryu360_rect=pygame.Rect(ryu.x-40,ryu.y,*self.Attack4_rect.size)
        if not user.character_select.Dead and not user.opponent_select.Dead and not user.opponent_select.Knockout and not user.character_select.Knockout  :
            if user.character_select==balrog  and current_time-self.last_collision_time>Attack_cooldown and user.character_select.Attacking :            
                if balroglpunch_rect.colliderect(pygame.Rect(target.x, target.y, *target.outline_rect.size)) and not target.Block and balrog.L_attack:
                    target.Head_hit=True
                    target.health-=5
                    self.last_collision_time=current_time
                    print(f"{target.health}")
                    hit.play()
                elif balrogrpunch_rect.colliderect(pygame.Rect(target.x, target.y, *target.outline_rect.size)) and not target.Block and balrog.R_attack:
                    target.health-=5
                    target.Body_hit=True
                    self.last_collision_time=current_time
                    print(f"{target.health}")
                    hit.play()
                elif balroguppercut_rect.colliderect(pygame.Rect(target.x, target.y, *target.outline_rect.size)) and not target.Block and balrog.Attack_3:
                    target.health-=10
                    target.Body_hit=True
                    print(f"{target.health}")
                    self.last_collision_time=current_time
                    hit.play()
## if not collided play miss sound
                elif not user.sound_played:
                    miss.play()
                    print('sound')
                    user.sound_played=True
                
            if user.character_select==ryu and current_time-self.last_collision_time>Attack_cooldown :
                 if ryulkick_rect.colliderect(pygame.Rect(target.x, target.y, *target.outline_rect.size)) and not target.Block and ryu.L_attack:
                    target.Head_hit=True
                    target.health-=5
                    self.last_collision_time=current_time
                    print(f"{target.health}")
                    hit.play()
                 elif ryurkick_rect.colliderect(pygame.Rect(target.x, target.y, *target.outline_rect.size)) and not target.Block and ryu.R_attack:
                    target.health-=5
                    target.Body_hit=True
                    self.last_collision_time=current_time
                    print(f"{target.health}")
                    hit.play()
                 
                 elif ryuaxe_rect.colliderect(pygame.Rect(target.x, target.y, *target.outline_rect.size)) and not target.Block and ryu.Attack_3:
                        target.health-=10
                        target.Head_hit=True
                        self.last_collision_time=current_time
                        print(f"{target.health}")
                        hit.play()
                 
                 elif ryu360_rect.colliderect(pygame.Rect(target.x, target.y, *target.outline_rect.size)) and not target.Block and ryu.Attack_4:
                        target.health-=10
                        target.Head_hit=True
                        self.last_collision_time=current_time
                        print(f"{target.health}")
                        hit.play()
                 elif not user.sound_played :
                    miss.play()
                    print('sound')
                    user.sound_played=True
                          
##    drawing animations + sprites
    def draw(self,screen):
            if  not self.x-self.vel>=0:
                self.x=1
            if not self.x+self.width<SCREEN_WIDTH:
                self.x=SCREEN_WIDTH-self.width
            if self.walkCount==35:
                self.walkCount=0
##  knockout animations
            if user.character_select.health<=0 and user.character_select.Knockout and not user.character_select.Dead :
                if user.character_select==ryu:
                    screen.blit(ryu_knockout[(self.walkCount//3)%7],(user.character_select.x,user.character_select.y))
                elif user.character_select==balrog:
                    screen.blit(balrog_knockout[(self.walkCount//3)%5],(user.character_select.x,user.character_select.y))
                self.walkCount+=1
##   dead animations            
            elif user.character_select.Dead   : 
                if user.character_select==ryu:
                    screen.blit(ryu_knockout[6],(user.character_select.x-150,user.character_select.y+30))
                elif user.character_select==balrog:
                    screen.blit(balrog_knockout[4],(user.character_select.x-80,user.character_select.y+30))
##               rest of the animations 
            elif user.character_select==balrog and not user.character_select.Dead :
                if self.Right and self.on_ground:
                  screen.blit(balrog_walking[(self.walkCount//3)%4],(self.x,self.y))                   
                elif self.Left and self.on_ground:
                   screen.blit(balrog_walking[(self.walkCount//3)%4],(self.x,self.y))                   
                elif self.Crouch and self.on_ground:
                   screen.blit(balrog_crouching[0],(self.x,self.y+(self.height//2)))                   
                elif self.Jump:
                   screen.blit(balrog_jumping[(self.jumpCount//3)%6],(self.x,self.y))                    
                elif self.L_attack:
                    screen.blit(balrog_L_attack[(self.walkCount//3)%3],(self.x,self.y))                  
                elif self.R_attack:
                    screen.blit(balrog_R_attack[(self.walkCount//2)%5],(self.x,self.y))                     
                elif self.Attack_3:
                    if user.selectedskill=='uppercut':
                        screen.blit(balrog_Attack_3[(self.walkCount//6)%3],(self.x,self.y))                     
                elif self.Head_hit:
                   screen.blit(balrog_head_reaction[(self.walkCount//6)%3],(self.x,self.y))                    
                elif self.Body_hit:
                   screen.blit(balrog_body_reaction[(self.walkCount//6)%3],(self.x,self.y+30))                    
                else  :
                    screen.blit(balrog_standing[(self.walkCount//3)%4],(self.x,self.y))
            elif user.character_select==ryu and not user.character_select.Dead :
                if self.Right and self.on_ground:
                  screen.blit(ryu_walking[(self.walkCount//3)%5],(self.x,self.y))                  
                elif self.Left and self.on_ground:
                    screen.blit(ryu_walking[(self.walkCount//3)%5],(self.x,self.y))                   
                elif self.Crouch and self.on_ground:
                   screen.blit(ryu_crouching[self.walkCount%1],(self.x,self.y+(self.height//3.8)))                    
                elif self.Jump:
                   screen.blit(ryu_jumping[(self.jumpCount//3)%7],(self.x,self.y))                   
                elif self.L_attack:
                    screen.blit(ryu_L_kick[(self.walkCount//2)%3],(self.x,self.y))                   
                elif self.R_attack:
                    screen.blit(ryu_R_kick[(self.walkCount//3)%3],(self.x,self.y))                     
                elif self.Attack_3:                   
                    screen.blit(ryu_Axe[(self.walkCount//3)%3],(self.x,self.y))
                elif self.Attack_4:
                    screen.blit(ryu_360[(self.walkCount//3)%10],(self.x,self.y))
                elif self.Head_hit:
                   screen.blit(ryu_head_reaction[(self.walkCount//6)%3],(self.x,self.y))                    
                elif self.Body_hit:
                   screen.blit(ryu_body_reaction[(self.walkCount//6)%3],(self.x,self.y))                   
                else  :
                    screen.blit(ryu_standing[(self.walkCount//3)%5],(self.x,self.y))
            self.walkCount+=1
      #rectangles for collision (testing)
##            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.x, self.y, *self.outline_rect.size), 2)           
##
##            pygamcse.draw.rect(screen,(255,165,0),pygame.Rect(user.character_select.x,user.character_select.y,*self.L_attack_rect.size),2)            
##            pygame.draw.rect(screen,(255,165,0),pygame.Rect(user.character_select.x,user.character_select.y,*self.R_attack_rect.size),2)
##            pygame.draw.rect(screen,(255,165,0),pygame.Rect(user.character_select.x,user.character_select.y,*self.uppercut_rect.size),2)
##resetting all variables to original (resetting game)
    def reset(self):
        self.health=100
        self.Head_hit=False
        self.Body_hit=False
        self.Left=False
        self.Right=False
        self.Crouch=False
        self.Block=False
        self.Jump=False
        self.L_attack=False
        self.R_attack=False
        self.Attack_3=False
        self.Attack_4=False
        self.Attacking=False
        self.Head_hit=False
        self.Body_hit=False
        self.Knockout=False
        self.Dead=False
        self.walkCount=0
        self.on_ground=True
        self.jumpCount=0
        self.attack_Count=0
        self.skillpoints=0
        if self.left_right=='left':
            self.x=100
        elif self.left_right=='right':
            self.x=800
            
## AI opponent class , takes in the character class
class Ai(character):
    def __init__(self,x,y,width,height,health,name,style,has_skillmove,left_right,target):
        super().__init__(x,y,width,height,health,name,style,has_skillmove,left_right,target)        
    def left(self):
        super().left()       
    def right(self):
        super().right()        
    def jump(self):
        super().jump()
    def crouch(self):
        super().crouch()
    def l_attack(self):        
        super().l_attack()
    def r_attack(self):        
        super().r_attack()
    def attack_3(self):
        super().attack_3()
    def knockout(self):
        super().knockout()
        
## updating variables for animation
    def update(self,current_time,GAME_MODE):
## if vs mode selected should inherit the update, otherwise it will be different as AI  
        if GAME_MODE=="VS":
            super().update(current_time)
        else:
            if  not self.x-self.vel>=0:
                    self.x=1
            if not self.x+self.width<SCREEN_WIDTH:
                    self.x=SCREEN_WIDTH-self.width
            if self.walkCount+1==36:
                    self.walkCount=0
            if self.Right and self.on_ground and not self.Attacking:
                   self.walkCount+=1
##making sure sprites animate for a while and not only a split second
                   if current_time-self.last_movement_time>=walk_cooldown:
                        self.Right=False
                        self.last_movement_time=current_time
            if self.Knockout:
                self.walkCount+=1
                self.attack_Count+=1
                if self.attack_Count==7:
                    print('dead')
                    self.Dead=True
                    self.Knockout=False
                    self.Attacking=False             
            elif self.Left and self.on_ground and not self.Attacking :
                   self.walkCount+=1
                   if current_time-self.last_movement_time>=walk_cooldown:
                       self.Left=False
                       self.last_movement_time=current_time
            elif self.Crouch and self.on_ground:
                    self.walkCount+=1
                    if current_time-self.last_movement_time>=Attack_cooldown:
                        self.Crouch=False
                        self.Block=False
                        self.last_movement_time=current_time
            #jumping mechanics
            if self.Jump:
                if self.jumpCount<6:
                    self. jumpCount+=1
                    
                self.y-=self.y_vel                
                self.y_vel-=gravity
                self.walkCount+=1
               
                if self.y>=150:
                    self.y=150
                    self.on_ground=True
                    self.Jump=False
            elif self.L_attack  :           
                    self.walkCount+=1
                    self.attack_Count+=1
                    if self.attack_Count==4:  
                        self.L_attack=False
                        self.Attacking=False
                        self.attack_Count=0                
                
            elif self.R_attack :               
                    self.walkCount+=1
                    self.attack_Count+=1
                    #when attack reaches final animation frame, set to false
                    if self.attack_Count==5  :
                        self.R_attack=False
                        self.Attacking=False
                        self.attack_Count=0
                        
            elif self.Attack_3  :               
                self.walkCount+=1
                self.attack_Count+=1
                if self.attack_Count==4  :
                    self.Attack_3=False
                    self.Attacking=False
                    self.attack_Count=0
                    
            elif self.Head_hit:
                self.walkCount+=1
                self.attack_Count+=1
                if self.attack_Count==3:
                    self.Head_hit=False
                    self.attack_Count=0
            elif self.Body_hit:
                self.walkCount+=1
                self.attack_Count+=1
                if self.attack_Count==3:
                    self.Body_hit=False
                    self.attack_Count=0
##        collision checking for opponent 
    def attack(self,target,current_time):        
        #collision rect for balrog2
        balrog2lpunch_rect=pygame.Rect((balrog2.x-balrog2.width/1.8)+40,balrog2.y,*self.L_attack_rect.size)
        balrog2rpunch_rect=pygame.Rect((balrog2.x-balrog2.width*1.43)+40,balrog2.y,*self.R_attack_rect.size)
        balrog2uppercut_rect=pygame.Rect((balrog2.x-balrog2.width*1.43)+40,balrog2.y,*self.uppercut_rect.size)

        #collision rect for ryu2
        ryu2lkick_rect=pygame.Rect((ryu2.x-80),ryu2.y,*self.L_kick_rect.size)
        ryu2rkick_rect=pygame.Rect((ryu2.x-20),ryu2.y,*self.R_kick_rect.size)
        ryu2axe_rect=pygame.Rect((ryu2.x-ryu2.width/2)+40,ryu2.y,*self.axe_rect.size)

        ##collision checking
        if not user.character_select.Dead and not user.opponent_select.Dead and not user.opponent_select.Knockout and not user.character_select.Knockout  :
            if user.opponent_select==balrog2 and current_time-self.last_collision_time>Attack_cooldown   :
                if balrog2lpunch_rect.colliderect(pygame.Rect(target.x, target.y, *target.outline_rect.size)) and not target.Block and balrog2.L_attack:
                     target.health-=5
                     target.Head_hit=True
                     self.last_collision_time=current_time
                     print(f"{target.health}")
                     hit.play()
                elif balrog2rpunch_rect.colliderect(pygame.Rect(target.x, target.y, *target.outline_rect.size)) and not target.Block and balrog2.R_attack:
                     target.health-=5
                     target.Body_hit=True
                     self.last_collision_time=current_time
                     print(f"{target.health}")
                     hit.play()
                elif balrog2uppercut_rect.colliderect(pygame.Rect(target.x, target.y, *target.outline_rect.size)) and not target.Block and balrog2.Attack_3:
                     target.health-=10
                     target.Body_hit=True
                     self.last_collision_time=current_time
                     print(f"{target.health}")
                     hit.play()
## miss sound if opponent attacks but doesnt hit
                elif not user.sound_played :
                    miss.play()
                    print('sound')
                    user.sound_played=True
            if user.opponent_select==ryu2 and current_time-self.last_collision_time>Attack_cooldown :
                 if ryu2lkick_rect.colliderect(pygame.Rect(target.x, target.y, *target.outline_rect.size)) and not target.Block and ryu2.L_attack:
                     target.health-=5
                     target.Head_hit=True
                     self.last_collision_time=current_time
                     print(f"{target.health}")
                     hit.play()
                 elif ryu2rkick_rect.colliderect(pygame.Rect(target.x, target.y, *target.outline_rect.size)) and not target.Block and ryu2.R_attack:
                     target.health-=5
                     target.Body_hit=True
                     self.last_collision_time=current_time
                     print(f"{target.health}")
                     hit.play()
                 elif ryu2axe_rect.colliderect(pygame.Rect(target.x, target.y, *target.outline_rect.size)) and not target.Block and ryu2.Attack_3:
                     target.health-=10
                     target.Head_hit=True
                     self.last_collision_time=current_time
                     print(f"{target.health}")
                     hit.play()
                 elif not user.sound_played :
                    miss.play()
                    print('sound')
                    user.sound_played=True
## drawing opponent sprites + animations 
    def draw(self,screen):
            if  not self.x-self.vel>=0:
                self.x=1
            if not self.x+self.width<SCREEN_WIDTH:
                self.x=SCREEN_WIDTH-self.width
            if self.walkCount==35:
                self.walkCount=0
## knockout animations
            if  user.opponent_select.health<=0 and user.opponent_select.Knockout and not user.opponent_select.Dead:                
                if  user.opponent_select==ryu2:
                    screen.blit(ryu_knockout_flip[(self.walkCount//3)%7],(user.opponent_select.x,user.opponent_select.y))
                elif user.opponent_select==balrog2:
                    screen.blit(balrog_knockout_flip[(self.walkCount//3)%5],(user.opponent_select.x,user.opponent_select.y))
                self.walkCount+=1
## dead animations
            elif user.opponent_select.Dead   : #and (user.opponent_select.Head_hit or user.opponent_select.Body_hit)
                if user.opponent_select==ryu2:
                    screen.blit(ryu_knockout_flip[6],(user.opponent_select.x+20,user.opponent_select.y+30))
                elif user.opponent_select==balrog2:
                    screen.blit(balrog_knockout_flip[4],(user.opponent_select.x,user.opponent_select.y+30))
##               rest of the animations         
            elif user.opponent_select==balrog2 and not user.opponent_select.Dead :
                 if self.Right and self.on_ground:                
                    screen.blit(balrog_walking_flip[(self.walkCount//3)%4],(self.x,self.y))
                 elif self.Left and self.on_ground:
                    screen.blit(balrog_walking_flip[(self.walkCount//3)%4],(self.x,self.y))
                 elif self.Crouch and self.on_ground:
                    screen.blit(balrog_crouching_flip[self.walkCount%1],(self.x,self.y+(self.height//2)))
                 elif self.Jump:
                     screen.blit(balrog_jumping_flip[self.jumpCount//3],(self.x,self.y))
                 elif self.L_attack:
                     img = balrog_L_attack_flip[(self.walkCount//3)%3]
                     screen.blit(img, img.get_rect(topright=(self.x+self.width , self.y)))
##                     screen.blit(balrog_L_attack_flip[(self.walkCount//3)%3],(self.x+self.width,self.y))
                 elif self.R_attack:
                     img = balrog_R_attack_flip[(self.walkCount//2)%5]                     
                     screen.blit(img, img.get_rect(topright=(self.x+self.width, self.y)))
                 elif self.Attack_3:
                     img = balrog_Attack_3_flip[(self.walkCount//6)%3]                     
                     screen.blit(img, img.get_rect(topright=(self.x+self.width, self.y)))
                 elif self.Head_hit:
                    img = balrog_head_reaction_flip[(self.walkCount//6)%3]                     
                    screen.blit(img, img.get_rect(topright=(self.x+self.width, self.y)))                 
                 elif self.Body_hit:
                    img = balrog_body_reaction_flip[(self.walkCount//6)%3]                     
                    screen.blit(img, img.get_rect(topright=(self.x+self.width, self.y+30)))
                 else  :
                     screen.blit(balrog_standing_flip[(self.walkCount//3)%4],(self.x,self.y))                        
            elif user.opponent_select==ryu2 and not user.opponent_select.Dead:
                 if self.Right and self.on_ground:
                     screen.blit(ryu_walking_flip[(self.walkCount//3)%5],(self.x,self.y))
                 elif self.Left and self.on_ground:
                     screen.blit(ryu_walking_flip[(self.walkCount//3)%5],(self.x,self.y))
                 elif self.Crouch and self.on_ground:
                     screen.blit(ryu_crouching_flip[self.walkCount%1],(self.x,self.y+(self.height//3.8)))
                 elif self.Jump:
                     screen.blit(ryu_jumping_flip[self.jumpCount//3],(self.x,self.y))
                 elif self.L_attack:
                     img = ryu_L_kick_flip[(self.walkCount//2)%3]
                     screen.blit(img, img.get_rect(topright=(self.x+self.width,self.y)))
                 elif self.R_attack:
                     img = ryu_R_kick_flip[(self.walkCount//3)%3]                     
                     screen.blit(img, img.get_rect(topright=(self.x+self.width, self.y)))
                 elif self.Attack_3:
                     img = ryu_Axe_flip[(self.walkCount//3)%3]                     
                     screen.blit(img, img.get_rect(topright=(self.x+self.width, self.y)))
                 elif self.Head_hit:
                     img = ryu_head_reaction_flip[(self.walkCount//6)%3]
                     screen.blit(img, img.get_rect(topright=(self.x+self.width, self.y)))
                 elif self.Body_hit:
                    img = ryu_body_reaction_flip[(self.walkCount//6)%3]                     
                    screen.blit(img, img.get_rect(topright=(self.x+self.width, self.y)))
                 else  :
                    screen.blit(ryu_standing_flip[(self.walkCount//3)%5],(self.x,self.y))
            self.walkCount+=1
            
  #attack rectangles for testing 
##            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.x, self.y, *self.outline_rect.size), 2)                     
##            pygame.draw.rect(screen,(255,165,0),pygame.Rect(user.opponent_select.x-user.opponent_select.width/1.8,user.opponent_select.y,*self.L_attack_rect.size),2)            
##            pygame.draw.rect(screen,(255,165,0),pygame.Rect(user.opponent_select.x-user.opponent_select.width*1.43,user.opponent_select.y,*self.R_attack_rect.size),2)
##            pygame.draw.rect(screen,(255,165,0),pygame.Rect(user.opponent_select.x-user.opponent_select.width/1.17,user.opponent_select.y,*self.uppercut_rect.size),2)

##random move selector for ai so that it chooses different attacks
    def random_attack(self):
        attack_select=random.choice([self.l_attack,self.r_attack,self.attack_3])                       
## checks if skill move is loaded so that the ai can use its skill move 
        if attack_select==self.attack_3:            
            print('3rd attack selected ')
            if user.opponent_select.skillmove_available:
                attack_select()
                user.opponent_select.skillmove_available=False
                user.opponent_select.skillpoints=0
        else:
            attack_select()        

## mechanics for ai opponent 
    def mechanics(self,difficulty,current_time,GAME_MODE,pause):
##    different difficulties will have different ratios for attacking and blocking 
        if GAME_MODE =="CAREER":
            if difficulty =="hard":
                move_ratio=0.1
                block_ratio=0.75
            elif difficulty=="intermediate":
                move_ratio=0.08
                block_ratio=0.5
            elif difficulty=="easy":
                move_ratio=0.04
                block_ratio=0.3
## calculates the distance between the players 
            distance = self.x-user.character_select.x
            if not self.Dead and not pause and not user.character_select.Dead and not (self.Head_hit or self.Body_hit) and not self.Knockout:
## checks if players are within fighting range  
                if distance<=SHORT_RANGE :
## using the blocking ratio if random is less than ratio and the user is attacking it will block (crouch)
                    if random.random()<block_ratio and user.character_select.Attacking :
                        self.crouch()
## if distance becomes less than 150 ai should move to avoid being too close 
                    elif distance <150:
                        self.right()
## incorporate random jumps and crouches when moving 
                        if random.random()<move_ratio  and self.on_ground : 
                            self.jump()
                            self.last_movement_time=current_time
                        elif random.random()<move_ratio and self.on_ground  : 
                            self.crouch()  
## if in fighting range and if random is less than ratio ai will attack 
                    elif  random.random()<move_ratio and current_time-self.last_attack_time>Attack_cooldown   :
                        self.random_attack()
                        self.last_attack_time=current_time                        
                else:
                    self.left()
## when moving incorporate random jumps and crouches 
                    if random.random()<move_ratio and self.on_ground  :
                        self.jump()                    
                        self.last_movement_time=current_time
                    elif random.random()<move_ratio and self.on_ground  : 
                        self.crouch()       

##   player class storing all data to be saved and used during game 
class Player():
    def __init__(self,money,has_skillmove):
        self.money=0
        self.has_skillmove=has_skillmove
        self.purchased=[False,False,False]
        self.savedgamename=False
        self.new_game_name=None
        self.error = False
        self.found= False
        self.last_error_time=0
        self.character_select=None
        self.opponent_select=None
        self.bg_select=bg_3
        self.game_data=[None,None,None,None,None,[False,False,False]]
        self.selectedskill=None
        self.opponentselectedskill='axe'
        self.checkedboxes=[False,False,False]
        self.sound_played=False
## method for purchasing skill in shop 
    def buy_skill(self,price,skillnumber):
##        if user has enough money and not already got the skill
         if self.money>=price and not self.purchased[skillnumber-1]:
             self.has_skillmove=True
             self.money-=price
             self.purchased[skillnumber-1]=True
             print("bought")
             Menu.savegame()
## errors
         elif self.money < price:
             self.error = True
             return self.error    
## updating users ability to use skill
    def update_skills(self,skillnumber):
        if self.purchased[skillnumber-1]==True:
            if skillnumber==1:
                ryu.has_skillmove=True
            elif skillnumber==3:
                ryu.has_skillmove=True
            elif skillnumber ==2:
                balrog.has_skillmove=True
##updating variables 
    def updatecharacter(self,name):
        self.character_select=name
    def updateopponent(self,name):
        self.opponent_select=name
    def updatebg(self,bg):
        self.bg_select=bg
## setting players targets 
    def set_targets(self):
        self.character_select.target=self.opponent_select
        self.opponent_select.target=self.character_select
                
#drawing healthbars and skill move bars 
def draw_healthbar(x,y,health,max_health):        
    ratio=health/max_health
    pygame.draw.rect(screen,(136, 8, 8),(x,y,200,20))
    pygame.draw.rect(screen,(34, 139, 34),(x,y,200*ratio,20))
def draw_skillmovebar(x,y,skillpoints,max_skillpoints,current_time,player_pick):        
    if current_time-player_pick.lastskillpointupdate>=skillpoint_cooldown and player_pick.skillpoints <100:
        player_pick.skillpoints+=0.5
        player_pick.lastskillpointupdate=current_time
    elif player_pick.skillpoints==100:
       player_pick.skillmove_available=True
    ratio=skillpoints/max_skillpoints
    pygame.draw.rect(screen,(255,255,255),(x,y,200,20))
    pygame.draw.rect(screen,(0, 0, 255),(x,y,200*ratio,20))
    
class Level():
##    level class for adjusting backrounds for each level as well as opponents and difficulty of game
    def __init__(self,level_number,background,opponent_select,difficulty):
        self.level_number=level_number
        self.background=background
        self.opponent_select=opponent_select
        self.difficulty=difficulty
##  adjusting level variables according to the level number the user is on
    def levelselect(self):        
        if self.level_number==1:
            print("here")
            self.background=bg_1
            self.opponent_select=ryu2
            self.difficulty="easy"
        elif self.level_number==2:
            self.background=bg_2
            self.opponent_select=balrog2
            self.difficulty="intermediate"
        elif self.level_number==3:
            self.background=bg_4
            self.opponent_select=ryu2
            self.difficulty="intermediate"
        elif self.level_number==4:
            self.background=bg_3
            self.opponent_select=balrog2
            self.difficulty="hard"
## button class
class Button():
    def __init__(self,image,x,y,text,font,text_colour):
        self.image=image
        self.x=x
        self.y=y
        self.text=text
        self.font=font
        self.text_colour=text_colour
        if self.text!=0:
            self.text_output=self.font.render(self.text,True,self.text_colour)
        if self.image==0:
            self.image=self.text_output
        self.rect=self.image.get_rect()
        self.rect.topleft=(self.x,self.y)
        
## drawing button
    def draw(self,rect):
        screen.blit(self.image,(self.x,self.y))
        if rect:
            pygame.draw.rect(screen,(255,0,0),self.rect,2)
    def update(self,text):
        self.text=text
        self.text_output=self.font.render(self.text,True,self.text_colour)
        self.image=self.text_output

##        check if hovering over button and able to press it 
    def checkifpress(self,mouse):
         if self.rect.collidepoint(mouse):
            return True
         else:
            return False
        
 ## draw all the features of the main game including healthbars and the characters  
def drawGameWindow(GAME_MODE,current_time):    
    if GAME_MODE=="VS":
        screen.blit(user.bg_select,(0,0))
    elif GAME_MODE=="CAREER":
        screen.blit(level.background,(0,0))
    draw_healthbar(50,20,user.character_select.health,100)
    draw_healthbar(750,20,user.opponent_select.health,100)
    draw_skillmovebar(50,50,user.character_select.skillpoints,100,current_time,user.character_select)
    draw_skillmovebar(750,50,user.opponent_select.skillpoints,100,current_time,user.opponent_select)
    if user.character_select==balrog:
        balrog.draw(screen)
    if user.character_select==ryu:
        ryu.draw(screen)
    if user.opponent_select==balrog2:
        balrog2.draw(screen)
    if user.opponent_select==ryu2 :
        ryu2.draw(screen)
    
    pygame.display.update()
class Menu():
    def updatestate(self,state_to_update):
        self.state=state_to_update
    def playmusic(self,state):
        pygame.mixer.music.load(music[state])
        pygame.mixer.music.play(-1)
## start screen function
    def StartScreen(self):
        self.playmusic('menu')
        while True :
    ##        menu_music.play()
            current_time=pygame.time.get_ticks()
            mouse=pygame.mouse.get_pos()
            screen.blit(intro_bg,(0,0))
            start_button=Button(start_img,425,280,0,0,0)
            start_button.draw(False)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if start_button.checkifpress(mouse):
                        click.play()
                        print("press")
                        self.start_options()
            pygame.display.update()

    ## start screen options function
    def start_options(self):
        while True :
            current_time=pygame.time.get_ticks()
            mouse=pygame.mouse.get_pos()
            screen.blit(intro_bg2,(0,0))
            startgame_button=Button(startgame_img,270,150,0,0,0)
            controls_button=Button(controls_img,370,260,0,0,0)
            credits_button=Button(credits_img,410,310,0,0,0)
            back_button=Button(back_img,5,30,0,0,0)
            back_button.draw(False)
            startgame_button.draw(False)
            controls_button.draw(False)
            credits_button.draw(False)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if startgame_button.checkifpress(mouse):
                        click.play()
                        self.load_new_vs()
                        
                    if controls_button.checkifpress(mouse):
                        click.play()
                        self.controls()                    
                    if credits_button.checkifpress(mouse):
                        click.play()
                        self.credits()
                        
                    if back_button.checkifpress(mouse):
                        click.play()
                        self.StartScreen()
            pygame.display.update()
    ##        options screen for after game is loaded (as shop shouldnt be visible before game is loaded )
    def options(self):
        while True :
            current_time=pygame.time.get_ticks()
            mouse=pygame.mouse.get_pos()
            screen.blit(intro_bg2,(0,0))
            startgame_button=Button(startgame_img,270,150,0,0,0)
            controls_button=Button(controls_img,370,250,0,0,0)
            shop_button=Button(shop_img,440,300,0,0,0)
            credits_button=Button(credits_img,420,350,0,0,0)
            back_button=Button(back_img,5,30,0,0,0)
            back_button.draw(False)
            startgame_button.draw(False)
            controls_button.draw(False)
            shop_button.draw(False)
            credits_button.draw(False)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if startgame_button.checkifpress(mouse):
                        click.play()
                        self.load_new_vs()
                    if controls_button.checkifpress(mouse):
                        click.play()
                        self.controls()
                    if shop_button.checkifpress(mouse):
                        click.play()
                        self.shop()
                    if credits_button.checkifpress(mouse):
                        click.play()
                        credits()
                    if back_button.checkifpress(mouse):
                        click.play()
                        self.StartScreen()
            pygame.display.update()
    ##choose which game mode to play, new game or load game or vs mode 
    def load_new_vs(self):
        while True :
            current_time=pygame.time.get_ticks()
            mouse=pygame.mouse.get_pos()
            screen.blit(intro_bg2,(0,0))
            loadgame_button=Button(loadgame_img,350,130,0,0,0)
            newgame_button=Button(newgame_img,370,230,0,0,0)
            vsmode_button=Button(vsmode_img,380,330,0,0,0)
            back_button=Button(back_img,5,30,0,0,0)
            back_button.draw(False)
            loadgame_button.draw(False)
            newgame_button.draw(False)        
            vsmode_button.draw(False)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if loadgame_button.checkifpress(mouse):
                        click.play()
                        self.loadgame()
                    if newgame_button.checkifpress(mouse):
                        GAME_MODE="CAREER"
                        click.play()
                        self.newgame()
                    if vsmode_button.checkifpress(mouse):
                        GAME_MODE="VS"
                        click.play()
                        self.characterselect(GAME_MODE)
                    if back_button.checkifpress(mouse):
                        click.play()
                        self.start_options()
            pygame.display.update()

    ## controls screen
    def controls(self):
        while True :
            current_time=pygame.time.get_ticks()
            mouse=pygame.mouse.get_pos()
            screen.blit(intro_bg2,(0,0))
            screen.blit(controllist_img,(225,125))
            back_button=Button(back_img,5,30,0,0,0)
            back_button.draw(False)

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if back_button.checkifpress(mouse):
                        click.play()
                        self.start_options()
                        
            pygame.display.update()

    ## credits screen
    def credits(self):
        while True :
            current_time=pygame.time.get_ticks()
            mouse=pygame.mouse.get_pos()
            screen.blit(intro_bg2,(0,0))
            screen.blit(credit_img,(250,225))
            back_button=Button(back_img,5,30,0,0,0)
            back_button.draw(False)
      
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if back_button.checkifpress(mouse):
                        click.play()
                        self.start_options()   
            pygame.display.update()

    ## shop screen , buy skill moves
    def shop(self):
        attacks_on_sale=[ryu_Axe[2],balrog_Attack_3[1],ryu_360[4]]
        shop_rectangle = [pygame.Rect(200, 150, 200, 200),pygame.Rect(425, 150, 200, 200),pygame.Rect(650,150, 200, 200)]    

        for i in range(len(attacks_on_sale)):            
    ## use scale factor to transform image of skill move to fit in rectangle 
            s_f=attacks_on_sale[i].get_height()/shop_rectangle[1].height
            img=pygame.transform.scale(attacks_on_sale[i],(shop_rectangle[0].width/s_f,shop_rectangle[0].height/s_f))
            attacks_on_sale[i]=img
        while True :
            current_time=pygame.time.get_ticks()
            mouse=pygame.mouse.get_pos()
            screen.blit(intro_bg2,(0,0))
            screen.blit(shop_img,(460,100))
            screen.blit(coin_img,(900,15))
            money_button=Button(0,950,20,f"{user.money}",pygame.font.SysFont("arial", 25),(255,255,255))
            for i in shop_rectangle:
                pygame.draw.rect(screen,(255,0,0),i,1)
            skillmove1_button=Button(attacks_on_sale[0],shop_rectangle[0].x+40,shop_rectangle[0].y+20,0,0,0)
            skillmove2_button=Button(attacks_on_sale[1],shop_rectangle[1].x+20,shop_rectangle[1].y+20,0,0,0)
            skillmove3_button=Button(attacks_on_sale[2],shop_rectangle[2].x+20,shop_rectangle[2].y+20,0,0,0)
            back_button=Button(back_img,5,30,0,0,0)
            buy1_button=Button(buy_img,330,280,0,0,0)
            buy2_button=Button(buy_img,555,280,0,0,0)
            buy3_button=Button(buy_img,780,280,0,0,0)
            checkbox1_button=Button(whitebox_img,220,300,0,0,0)
            checkbox2_button=Button(whitebox_img,445,300,0,0,0)
            checkbox3_button=Button(whitebox_img,670,300,0,0,0)
            checkedbox1_button=Button(checkedbox_img,220,300,0,0,0)
            checkedbox2_button=Button(checkedbox_img,445,300,0,0,0)
            checkedbox3_button=Button(checkedbox_img,670,300,0,0,0)
    ##        if skill move is purchased, draw the checkbox so that the user can select it as their chosen skill move
            if user.purchased[0]==True:
                checkbox1_button.draw(False)
            if user.purchased[1]==True:
                checkbox2_button.draw(False)
            if user.purchased[2]==True:
                checkbox3_button.draw(False)
                
    ##        if box is checked draw a checked box over it    
            if user.checkedboxes[0]==True:
                checkedbox1_button.draw(True)
            if user.checkedboxes[1]==True:
                checkedbox2_button.draw(True)
            if user.checkedboxes[2]==True:
                checkedbox3_button.draw(True)
                                      
            back_button.draw(False)
            money_button.draw(False)
            skillmove1_button.draw(False)
            skillmove2_button.draw(False)
            skillmove3_button.draw(False)
            buy1_button.draw(False)
            buy2_button.draw(False)
            buy3_button.draw(False)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if back_button.checkifpress(mouse):
                        click.play()
                        self.options()
                    if buy1_button.checkifpress(mouse) and user.character_select==ryu:
                        click.play()
                        user.buy_skill(50,1)
                        user.update_skills(1)
                    elif buy1_button.checkifpress(mouse):
                        user.error=True
                    if buy2_button.checkifpress(mouse) and user.character_select==balrog:
                        click.play()
                        user.buy_skill(50,2)
                        user.update_skills(2)
                    elif buy2_button.checkifpress(mouse):
                        user.error=True
                    if buy3_button.checkifpress(mouse) and user.character_select==ryu: 
                        click.play()
                        user.buy_skill(100,3)
                        user.update_skills(3)
                    elif buy3_button.checkifpress(mouse):
                        user.error=True
                    if checkedbox1_button.checkifpress(mouse) and user.character_select==ryu and user.purchased[0]==True:
                        click.play()
                        user.selectedskill='axe'
                        user.checkedboxes[0]=True
                        user.checkedboxes[2]=False
                        self.savegame()
                    if checkedbox2_button.checkifpress(mouse)  and user.character_select==balrog and user.purchased[1]==True:
                        click.play()
                        user.selectedskill='uppercut'
                        user.checkedboxes[1]=True
                        self.savegame()
                    if checkedbox3_button.checkifpress(mouse)  and user.character_select==ryu and user.purchased[2]==True :
                        click.play()
                        user.selectedskill='360'
                        user.checkedboxes[2]=True
                        user.checkedboxes[0]=False
                        self.savegame()
            if user.error == True :
                #print("Error initiated!")
                screen.blit(error_img,(10,420))            
            if current_time -1000>user.last_error_time:
                user.last_error_time=current_time
                user.error=False
            if skillmove1_button.checkifpress(mouse):
                shop_rectangle[0].height=300
                screen.blit(specialmovedescription1_img,(200,340))
            elif not skillmove1_button.checkifpress(mouse):
                shop_rectangle[0].height=200            
            if skillmove2_button.checkifpress(mouse):
                shop_rectangle[1].height=300
                screen.blit(specialmovedescription2_img,(425,340))
            elif not skillmove2_button.checkifpress(mouse):
                shop_rectangle[1].height=200
            if skillmove3_button.checkifpress(mouse):
                shop_rectangle[2].height=300
                screen.blit(specialmovedescription3_img,(650,340))
            elif not skillmove3_button.checkifpress(mouse):
                shop_rectangle[2].height=200
            pygame.display.update()
    ## load game screen
    def loadgame(self):
        pressed = False
        in_text=''
        textbox_button=Button(textbox_img,250,270,'savedgamename',pygame.font.SysFont("arial", 30),(255,255,255))
        entered=False
        user.found=False

        while True :
            current_time=pygame.time.get_ticks()
            mouse=pygame.mouse.get_pos()
            screen.blit(intro_bg2,(0,0))
            screen.blit(enteryoursaved_img,(250,150))
            screen.blit(gamename_img,(330,210))         
            back_button=Button(back_img,5,30,0,0,0)
            back_button.draw(False)
            textbox_button.draw(True)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if back_button.checkifpress(mouse):
                        click.play()
                        self.load_new_vs()
                    if textbox_button.checkifpress(mouse):
                        click.play()
                        pressed = True
    ## typing the game name in (only select characters available to enter )
                if event.type==pygame.KEYDOWN:
                    if pressed and not event.key==pygame.K_RETURN and pygame.key.name(event.key)in available_characters and not entered and len(in_text)<16:
                        in_text+=event.unicode
                        textbox_button.text=in_text
                        textbox_button.update(in_text)
    ## backspace deleting characters
                    if pressed and event.key==pygame.K_BACKSPACE and not entered :
                        in_text=in_text[:-1]
                        print(in_text)
                        textbox_button.text=in_text
                        textbox_button.update(in_text)
    ## enter game name
                    elif event.key==pygame.K_RETURN and len(in_text)>5:
                        click.play()
                        user.savedgamename=textbox_button.text
    ## checking if game is already saved into text file, if not show error 
                        if  self.checkforsavedgame(user.savedgamename)==False or len(in_text)<5:
                             user.error=True
                        else:
                             entered=True
                             user.found=True
                if user.savedgamename!=False:
                    self.checkforsavedgame(user.savedgamename)
            if user.found:
                print(f"!!!!!!!!!!!!!{user.savedgamename}") 
                user.game_data=self.checkforsavedgame(user.savedgamename)
                print(f"!!!!!!!!!!!!!{user.game_data}")
    ## converting saved game data into right type of data (list/objects) 
                if user.game_data[2] in globals():
                    user.character_select=globals()[user.game_data[2]]
                level.level_number=int(user.game_data[1])
                level.levelselect()
                user.game_data[5]=eval((user.game_data[5]+","+user.game_data[6]+","+user.game_data[7]))
                del user.game_data[7],user.game_data[6]
                user.purchased=user.game_data[5]
                print(user.purchased)
                user.money=int(user.game_data[3])
                user.selectedskill=str(user.game_data[4])
                print(f"{user.selectedskill} ==     [user.game_data[4]]")
                user.updateopponent(level.opponent_select)
                user.set_targets()
                self.maingame("CAREER")
            if user.error == True   :
                print("Error initiated!")
                screen.blit(error_img,(10,420))
    ## make error only last for a second 
            if current_time-1000>user.last_error_time:
                user.last_error_time=current_time
                user.error=False
            pygame.display.update()
            entered=False
            
    ## new game screen 
    def newgame(self):
        GAME_MODE='CAREER'
        pressed = False
        in_text=''
        textbox_button=Button(textbox_img,250,270,'newgamename ',pygame.font.SysFont("arial", 30),(255,255,255))
        entered=False
        level.level_number=1
    ##    user.money=0
        user.purchased=[False,False,False]
        user.checkedboxes=[False,False,False]
        user.selectedskill=None
        while True :
            current_time=pygame.time.get_ticks()
            mouse=pygame.mouse.get_pos()
            screen.blit(intro_bg2,(0,0))
            screen.blit(enteryournew_img,(250,150))
            screen.blit(gamename_img,(330,210))         
            back_button=Button(back_img,5,30,0,0,0)
            back_button.draw(False)
            textbox_button.draw(True)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if back_button.checkifpress(mouse):
                        click.play()
                        self.load_new_vs()
                    if textbox_button.checkifpress(mouse):
                        click.play()
                        pressed = True
    ## entering new game name as well as backspace for deleting characters 
                if event.type==pygame.KEYDOWN:
                    if pressed and not event.key==pygame.K_RETURN and pygame.key.name(event.key)in available_characters and not entered and len(in_text)<16:
                        in_text+=event.unicode
                        textbox_button.text=in_text
                        textbox_button.update(in_text)
                    if pressed and event.key==pygame.K_BACKSPACE and not entered :
                        in_text=in_text[:-1]
                        print(in_text)
                        textbox_button.text=in_text
                        textbox_button.update(in_text)
                    elif event.key==pygame.K_RETURN and len(in_text)>5:
                         click.play()
                         user.new_game_name=textbox_button.text
                         if self.checkforsavedgame(user.new_game_name) or len(in_text)<5:
                             user.error=True
                         else:
                             entered=True
                             print(f"level number ={level.level_number}")
                             level.levelselect()
                             self.characterselect(GAME_MODE)
                             self.writegamedata()
            if user.error == True   :
                screen.blit(error_img,(10,420))
            if current_time-1000>user.last_error_time:
                user.last_error_time=current_time
                user.error=False
            pygame.display.update()

    ## writing game data to text file 
    def writegamedata(self):
        if user.new_game_name ==None:
            user.new_game_name=user.savedgamename
        game_data=open("game records.txt","a")
        data_to_save=[user.new_game_name,level.level_number,user.character_select.name,user.money,user.selectedskill,user.purchased]
        for i in data_to_save:
            game_data.write(str(i)+",")
        game_data.write("\n")
        game_data.close()
        user.game_data=self.checkforsavedgame(user.new_game_name)
        print(user.game_data)

    ## organising the data into the right format 
    def organisingsavedgamedata(self):
        organised_data=[]     
        game_data=open("game records.txt","r")
        for i in game_data:
            item=i.strip().rstrip(",")
            item=item.split(",")
            organised_data.append(item)
        game_data.close()
        return(organised_data)

    ## character select screen (choose characters)
    def characterselect(self,GAME_MODE):
        user.updateopponent(ryu2)
    ## if vs mode 2 characters to select
        if GAME_MODE=="VS":
            selected=[False,False]
        elif GAME_MODE=="CAREER":
            selected=[False]
        while True :
            current_time=pygame.time.get_ticks()
            mouse=pygame.mouse.get_pos()
            screen.blit(intro_bg2,(0,0))
            screen.blit(chooseyourcharacter_img,(150,40))
            characterselect_button=Button(characterselect_img,300,90,0,0,0)
            balrogselect_button=Button(balrogselect_img,301,205,0,0,0)
            ryuselect_button=Button(balrogselect_img,365,105,0,0,0)
            back_button=Button(back_img,5,30,0,0,0)
            back_button.draw(False)
            characterselect_button.draw(False)
           
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if balrogselect_button.checkifpress(mouse):
                        click.play()
    ## checking if characters have been selected 
                        if len(selected)==2  :
                            if selected[0]==True:
                                user.updateopponent(balrog2)
                                selected[1]=True
                                
                            elif selected[0]==False:
                                user.updatecharacter(balrog)
                                selected[0]=True 
    ## check if all of the characters that were meant to be selected have been selected
                            if all(selected):
                                user.set_targets()
                                self.selectlocation()
                                
                        else:
                            user.updatecharacter(balrog)
                            user.set_targets()
                            self.writegamedata()
                            self.maingame("CAREER")
                    if ryuselect_button.checkifpress(mouse):
                        click.play()
                        if len(selected)==2  :
                            if selected[0]==True:
                                user.updateopponent(ryu2)
                                selected[1]=True
                                
                            elif selected[0]==False:
                                user.updatecharacter(ryu)
                                selected[0]=True 
                            if all(selected):
                                user.set_targets()
                                self.selectlocation()
                        else:
                            user.updatecharacter(ryu)
                            user.set_targets()
                            self.writegamedata()
                            self.maingame("CAREER")
                    if back_button.checkifpress(mouse):
                        click.play()
                        self.load_new_vs()
            if ryuselect_button.checkifpress(mouse):                
                screen.blit(ryupreview_img,(0,150))            
            if balrogselect_button.checkifpress(mouse):
                screen.blit(balrogpreview_img,(0,150))
            
            pygame.display.update()
    ## selecting game location screen
    def selectlocation(self):
        selected=False
        GAME_MODE="VS"
        user.character_select.has_skillmove=True
        user.opponent_select.has_skillmove=True
        if user.character_select==balrog:
            user.selectedskill='uppercut'
        if user.opponentselectedskill==balrog2:
            user.opponentselectedskill='uppercut'
        if user.character_select==ryu:
            user.selectedskill='360'
        while True :
            current_time=pygame.time.get_ticks()
            mouse=pygame.mouse.get_pos()
            screen.blit(intro_bg2,(0,0))
            screen.blit(selectlocation_img,(250,40))
            background1_button=Button(background1_img,300,100,0,0,0)
            background2_button=Button(background2_img,520,100,0,0,0)
            background3_button=Button(background3_img,300,300,0,0,0)
            background4_button=Button(background4_img,520,300,0,0,0)
            back_button=Button(back_img,5,30,0,0,0)
            back_button.draw(False)
            background1_button.draw(False)
            background2_button.draw(False)
            background3_button.draw(False)
            background4_button.draw(False)
           
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if background1_button.checkifpress(mouse):
    ## when button is clicked plays clicking sound
                        click.play()
                        user.updatebg(bg_1)
                        selected=True                        
                    if background2_button.checkifpress(mouse):
                        click.play()
                        user.updatebg(bg_2)
                        selected=True
                    if background3_button.checkifpress(mouse):
                        click.play()
                        user.updatebg(bg_3)
                        selected=True                        
                    if background4_button.checkifpress(mouse):
                        click.play()
                        user.updatebg(bg_4)
                        selected=True 
                    if back_button.checkifpress(mouse):
                        click.play()
                        self.characterselect(GAME_MODE)
                    if selected:
                        self.maingame(GAME_MODE)        
            pygame.display.update()
    ##     check for saved game    
    def checkforsavedgame(self,name):
        read=self.organisingsavedgamedata()
        for i in read:
            if str(name) ==i[0]:
                print("file found")
                user.found=True
    ## return the game data so that it can be accessed
                return (i)
                print(f"i={i}")
        if not user.found:
            print("none")
            user.error=True
            return False

    ## save game function 
    def savegame(self):
        if user.new_game_name ==None:
            user.new_game_name=user.savedgamename
        data=self.checkforsavedgame(user.new_game_name)
        linecount=0
        print(f"data={data}")
        file=open("game records.txt","r+")
        lines=file.readlines()
        
        print(f"OLD LINES{lines}")
        for line in lines:        
            if data[0]==line.split(',')[0]:
                print(data[0])
                print(f"LINES BEING DELETED ({lines[linecount]})")
    ## deletes old game data and replaces it with the new data
                del lines[linecount]
    ##            print(f"NEW FILE{lines}")
            else:
                linecount+=1
        print(linecount)
        file.close()
        file=open("game records.txt","w")
        print(f"LINES-{lines}")
        file.writelines(lines)
        file.close()
        self.writegamedata()

    ## pause controls screen
##    def Pausecontrols(self,pausecontrols):
##        while pausecontrols:
##            current_time=pygame.time.get_ticks()
##            mouse=pygame.mouse.get_pos()
##            screen.blit(intro_bg2,(0,0))
##            screen.blit(controllist_img,(225,125))
##            back_button=Button(back_img,5,30,0,0,0)
##            back_button.draw(False)
##
##            for event in pygame.event.get():
##                if event.type==pygame.QUIT:
##                    pygame.quit()
##                    exit()
##                if event.type==pygame.MOUSEBUTTONDOWN:
##                    if back_button.checkifpress(mouse):
##                        click.play()
##                        pausecontrols=False       
##            pygame.display.update()

    ##        pause screen
    def Pause(self,pause):
##        pausecontrols=False
        if pause:
            pygame.draw.rect(blurred_screen,(128,128,128,10),[0,0,SCREEN_WIDTH,SCREEN_HEIGHT])
            screen.blit(blurred_screen,(0,0))
            current_time=pygame.time.get_ticks()
            mouse=pygame.mouse.get_pos()
    ##        startgame_button=Button(startgame_img,270,150,0,0,0)
    ##        controls_button=Button(controls_img,370,250,0,0,0)
##            quit_button=Button(quit_img,450,320,0,0,0)
##            quit_button.draw(False)
##    ##        startgame_button.draw(False)
##    ##        controls_button.draw(False)
##            for event in pygame.event.get():
##                if event.type==pygame.QUIT:
##                    pygame.quit()
##                    exit()
##                if event.type==pygame.MOUSEBUTTONDOWN:
    ##                if startgame_button.checkifpress(mouse):
    ##                    print('pressed')
    ##                    click.play()
    ##                    pause=False
    ##                if controls_button.checkifpress(mouse):
    ##                    print('pressed')
    ##                    click.play()
    ##                    pausecontrols=True
    ##                    Pausecontrols(pausecontrols)
##                    if quit_button.checkifpress(mouse):
##                        print('pressed')
##                        click.play()
##                        self.playmusic('menu')
##                        user.character_select.reset()
##                        user.opponent_select.reset()
##                        self.options()
##                if event.type == pygame.KEYDOWN:
##                        if event.key ==pygame.K_SPACE  :
##                            
##                            pause=False           
        pygame.display.update() 
        
    ## when player 1 wins (vs mode) show this screen 
    def player1winner(self):
        self.playmusic('winner')
        user.character_select.reset()
        user.opponent_select.reset()
        user.set_targets()
        while True :
            current_time=pygame.time.get_ticks()
            mouse=pygame.mouse.get_pos()
            screen.blit(intro_bg2,(0,0))
            screen.blit(player1_img,(270,10))
            screen.blit(winner_img,(220,120))
            quit_button=Button(winnerquit_img,450,320,0,0,0)
            restart_button=Button(restart_img,400,260,0,0,0)
            quit_button.draw(False)
            restart_button.draw(False)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if quit_button.checkifpress(mouse):
                        click.play()
                        self.playmusic('menu')
                        self.start_options()
                    if restart_button.checkifpress(mouse):
                        click.play()
                        self.characterselect('VS')
                        
            pygame.display.update()

    ## when player 2 wins (vs mode) show this screen         
    def player2winner(self):
        self.playmusic('winner')
    ## resetting values for next game
        user.character_select.reset()
        user.opponent_select.reset()
        user.set_targets()
        while True :
            current_time=pygame.time.get_ticks()
            mouse=pygame.mouse.get_pos()
            screen.blit(intro_bg2,(0,0))
            screen.blit(player2_img,(270,10))
            screen.blit(winner_img,(220,120))
            quit_button=Button(winnerquit_img,450,320,0,0,0)
            restart_button=Button(restart_img,400,260,0,0,0)
            quit_button.draw(False)
            restart_button.draw(False)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if quit_button.checkifpress(mouse):
                        click.play()
                        self.playmusic('menu')
                        self.start_options()
                    if restart_button.checkifpress(mouse):
                        click.play()
                        self.characterselect('VS')
                        
            pygame.display.update()

    ## winner screen for career mode 
    def winner(self,GAME_MODE):
        self.playmusic('winner')
        user.character_select.reset()
        user.opponent_select.reset()
        user.game_data[1]=int(user.game_data[1])+1
        level.level_number=int(user.game_data[1])
        level.levelselect()
        user.updateopponent(level.opponent_select)
        user.set_targets()
        original_money=user.money
        while True :
            current_time=pygame.time.get_ticks()
            mouse=pygame.mouse.get_pos()
            screen.blit(intro_bg2,(0,0))
            screen.blit(winner_img,(220,120))
            quit_button=Button(winnerquit_img,450,320,0,0,0)
            nextlevel_button=Button(nextlevel_img,350,260,0,0,0)
            screen.blit(coin_img,(900,15))
            money_button=Button(0,950,20,f"{user.money}",pygame.font.SysFont("arial", 25),(255,255,255))
            money_button.draw(False)
            quit_button.draw(False)
            nextlevel_button.draw(False)
            if user.money < original_money+25:
                user.money+=1
                if user.money==original_money+25:
                    self.savegame()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if quit_button.checkifpress(mouse):
                        click.play()
                        self.playmusic('menu')
                        self.options()
                        
                    if nextlevel_button.checkifpress(mouse):
                        click.play()
                        self.maingame(GAME_MODE)
            pygame.display.update()
            
    ##    defeat screen for career mode 
    def defeat(self,GAME_MODE):
        self.playmusic('defeat')
        user.character_select.reset()
        user.opponent_select.reset()
        while True :
            current_time=pygame.time.get_ticks()
            mouse=pygame.mouse.get_pos()
            screen.blit(intro_bg2,(0,0))
            screen.blit(defeat_img,(250,120))        
            restart_button=Button(restart_img,400,260,0,0,0)
            quit_button=Button(quit_img,450,320,0,0,0)
            screen.blit(coin_img,(900,15))
            money_button=Button(0,950,20,f"{user.money}",pygame.font.SysFont("arial", 25),(255,255,255))
            money_button.draw(False)
            quit_button.draw(False)
            restart_button.draw(False)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if quit_button.checkifpress(mouse):
                        click.play()
                        self.playmusic('menu')
                        self.options()
                    if restart_button.checkifpress(mouse):
                        click.play()
                        self.maingame(GAME_MODE)
            pygame.display.update()

    ## champion screen for when user wins 4 fights 
    def champion(self):
        self.playmusic('champion')
        user.character_select.reset()
        user.opponent_select.reset()
        original_money=user.money
        while True :
            current_time=pygame.time.get_ticks()
            mouse=pygame.mouse.get_pos()
            screen.blit(championbg_img,(0,0))
            screen.blit(champion_img,(140,90))
            screen.blit(belt_img,(355,130))
            defendtitle_button=Button(defendtitle_img,336,350,0,0,0)
            quit_button=Button(quit_img,449,400,0,0,0)
            screen.blit(coin_img,(900,15))
            money_button=Button(0,940,20,f"{user.money}",pygame.font.SysFont("arial", 25),(255,255,255))
            money_button.draw(False)
            quit_button.draw(False)
            defendtitle_button.draw(False)
    ## add by 1 so the user can see it rising 
            if user.money < original_money+50:
                user.money+=1
    ## when reaches the amount it should reach savegame
                if user.money==original_money+50:
                    self.savegame()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if quit_button.checkifpress(mouse):
                        click.play()
                        self.playmusic('menu')
                        self.options()
                    if defendtitle_button.checkifpress(mouse):
                        click.play()
                        self.maingame('CAREER')
                    
            pygame.display.update()
    
    ##main game loop
    def maingame(self,GAME_MODE):    
        pause =False
        self.playmusic('maingame')
        while True :
            pygame.time.delay(40)
            clock.tick(36)
            current_time=pygame.time.get_ticks()
            mouse=pygame.mouse.get_pos()
            if pause:
                self.Pause(pause)
            if  user.character_select.health<=0 and not user.character_select.Dead:
                user.character_select.knockout()
            if  user.opponent_select.health<=0 and not user.opponent_select.Dead :
                user.opponent_select.knockout()
    ## show end of game screens (winner/defeat) when either player loses  
            if  user.opponent_select.Dead:
                time.sleep(2)
                if GAME_MODE=='VS':
                    self.player1winner()
                elif level.level_number <4 :
                    self.winner(GAME_MODE)
                else:
                    self.champion()
            elif user.character_select.Dead:
                time.sleep(2)
                if GAME_MODE=='VS':
                    self.player2winner()
                else:
                    self.defeat(GAME_MODE)
                    self.savegame()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    exit()
        ##            running=False
        ##        current_time=pygame.time.get_ticks()

    ##            when keys are pressed initialise movements (attacking/moving)
                if event.type == pygame.KEYDOWN and not pause and not user.character_select.Attacking and not user.character_select.Jump and user.character_select.on_ground and current_time-user.character_select.last_attack_time>Attack_cooldown and not user.character_select.Crouch  and not user.character_select.Dead :
                    if event.key == pygame.K_x  :
                        user.character_select.l_attack()
                        user.character_select.last_attack_time=current_time
                    elif event.key == pygame.K_c :
                        user.character_select.r_attack()
                        user.character_select.last_attack_time=current_time
                    elif event.key == pygame.K_v and user.character_select.skillmove_available: #and user.character_select.has_skillmove 
                        if user.selectedskill=='uppercut' or user.selectedskill== 'axe' :
                            user.character_select.attack_3()
                            user.character_select.last_attack_time=current_time
                            user.character_select.skillmove_available=False
                            user.character_select.skillpoints=0
                        elif user.selectedskill==('360'):
                            user.character_select.attack_4()
                            user.character_select.last_attack_time=current_time
                            user.character_select.skillmove_available=False
                            user.character_select.skillpoints=0
                        
                    elif event.key == pygame.K_w:
                        user.character_select.jump()
                        user.character_select.last_attack_time=current_time
                if event.type == pygame.KEYDOWN:
    ## pausing game 
                    if event.key ==pygame.K_SPACE  :
                        if pause==True:
                            pause=False
##                            pygame.mixer.music.unpause()
                        else:
                            pause=True
##                            pygame.mixer.music.pause()
                        print('pause')
    ## if vs mode , initialise player 2s movements ( not needed for career mode )
                if GAME_MODE=="VS":
                    if event.type == pygame.KEYDOWN and not pause and not user.opponent_select.Attacking and not user.opponent_select.Jump and user.opponent_select.on_ground and current_time-user.opponent_select.last_attack_time>Attack_cooldown and not user.opponent_select.Crouch and not user.opponent_select.Dead  :
                        if event.key == pygame.K_UP :
                            user.opponent_select.jump()
                            user.opponent_select.last_attack_time=current_time
                        elif event.key == pygame.K_p :
                            user.opponent_select.l_attack()
                            user.opponent_select.last_attack_time=current_time
                        elif event.key == pygame.K_o :
                            user.opponent_select.r_attack()
                            user.opponent_select.last_attack_time=current_time
                        elif event.key == pygame.K_i and user.opponent_select.skillmove_available:
                            user.opponent_select.attack_3()
                            user.opponent_select.last_attack_time=current_time
                            user.opponent_select.skillmove_available=False
                            user.opponent_select.skillpoints=0
                     
            user.opponent_select.mechanics(level.difficulty,current_time,GAME_MODE,pause)
            if user.character_select.Attacking:
                user.character_select.attack(user.character_select.target,current_time)            
            elif user.opponent_select.Attacking:
                user.opponent_select.attack(user.opponent_select.target,current_time)
            
            user.character_select.update(current_time)
            user.opponent_select.update(current_time,GAME_MODE)
        ##player1 left/right controls

            keys=pygame.key.get_pressed()
            if not user.character_select.Attacking and not pause and not user.character_select.Head_hit and not user.character_select.Body_hit and user.character_select.health>0  :
                if keys[pygame.K_a] :
                     user.character_select.left()
                elif keys[pygame.K_d] and user.character_select.x+80<user.opponent_select.x   :
                     user.character_select.right()
            ##crouch + block
                elif keys[pygame.K_s]:
                     user.character_select.crouch()
            
            
        ##player2 controls
            if GAME_MODE=="VS":
                if not user.opponent_select.Attacking and not pause and not user.opponent_select.Head_hit and not user.opponent_select.Body_hit and user.opponent_select.health>0  :
                    if keys[pygame.K_LEFT] and user.character_select.x+80<user.opponent_select.x and not user.opponent_select.Head_hit and not user.opponent_select.Body_hit  and user.opponent_select.health>0 and not user.character_select.Attacking :
                        user.opponent_select.left()
                    elif keys[pygame.K_RIGHT] and not user.opponent_select.Head_hit and not user.opponent_select.Body_hit  and user.opponent_select.health>0 :
                        user.opponent_select.right()
                ##crouch
                    elif keys[pygame.K_DOWN]:
                        user.opponent_select.crouch()
            if not pause:
                drawGameWindow(GAME_MODE,current_time)        
    
clock=pygame.time.Clock()   
user=Player(0,False)
balrog=character(100,150,150,100,100,'balrog','boxer',False,'left',' ')
balrog2=Ai(800,150,150,100,100,'balrog2','boxer',False,'right',' ')
ryu=character(100,150,150,100,100,'ryu','kicker',False,'left',' ')
ryu2=Ai(800,145,150,100,100,'ryu2','kicker',False,'right',' ')
level=Level(None,None,ryu2,None)
Menu=Menu()
timer=0
delay=1    
   
Menu.StartScreen()

