# Writing entirely in lowercase or using indoor voice
def Av(Voice):
    Voice = Voice.strip().lower().capitalize()
    print(Voice)
Av(input("Say it here: "))



# Playback speed
def vi():
    Speed = input("")
    Speed = Speed.replace(" ", "...")
    print(f"{Speed}")
vi()