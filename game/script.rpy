# 이 파일에 게임 스크립트를 입력합니다.

define gui.text_color = "#402000"
define gui.text_font = "SCDream4.otf"


# image 문을 사용해 이미지를 정의합니다.


image bg select_food1 = "1.png"
image bg bg_river = "background/bg_river.jpg"
image bg bg_forest = "background/bg_forest.jpg"

image white = Solid("#fff")
image black = Solid("#000")

image bjorsson_normal:
    im.FactorScale("bjorsson/bjorsson_normal.png", 0.6)

image bjorsson_normal_dark:
    im.FactorScale("bjorsson/bjorsson_normal_dark.png", 0.6)

image helga_happy:
    im.FactorScale("helga/helga_happy.png", 0.6)

image helga_happy_dark:
    im.FactorScale("helga/helga_happy_dark.png", 0.6)

image helga_normal:
    im.FactorScale("helga/helga_normal.png", 0.6)

image helga_normal_dark:
    im.FactorScale("helga/helga_normal_dark.png", 0.6)
    
image helga_sad:
    im.FactorScale("helga/helga_sad.png", 0.6)

image helga_sad_dark:
    im.FactorScale("helga/helga_sad_dark.png", 0.6)

image chonjang_happy:
    im.FactorScale("chonjang/chonjang_happy.png", 0.6)

image chonjang_happy_dark:
    im.FactorScale("chonjang/chonjang_happy_dark.png", 0.6)

image chonjang_normal:
    im.FactorScale("chonjang/chonjang_normal.png", 0.6)

image chonjang_normal_dark:
    im.FactorScale("chonjang/chonjang_normal_dark.png", 0.6)

image ivar_happy:
    im.FactorScale("ivar/ivar_happy.png", 0.6)

image ivar_happy_dark:
    im.FactorScale("ivar/ivar_happy_dark.png", 0.6)

image ivar_normal:
    im.FactorScale("ivar/ivar_normal.png", 0.6)

image ivar_normal_dark:
    im.FactorScale("ivar/ivar_normal_dark.png", 0.6)

image tulbug_happy:
    im.FactorScale("tulbug/tulbug_happy.png", 0.6)

image tulbug_happy_dark:
    im.FactorScale("tulbug/tulbug_happy_dark.png", 0.6)

image tulbug_normal:
    im.FactorScale("tulbug/tulbug_normal.png", 0.6)

image tulbug_normal_dark:
    im.FactorScale("tulbug/tulbug_normal_dark.png", 0.6)


# 게임에서 사용할 캐릭터를 정의합니다.
define b = Character('비욘슨', color = "#ebd660", what_slow_cps = 20)
define c = Character('촌장', color = "658c6a", what_slow_cps = 20)
define h = Character('헬가', color = "862041", what_slow_cps = 20)
define i = Character('아이바르', color = "467171", what_slow_cps =20)
define t = Character('툴부그', color = "948d82", what_slow_cps = 20)

screen Day1:
    imagebutton:
        idle 'tulbug/tulbug_full_dark.png' hover 'tulbug/tulbug_full.png'
        action Jump('tulbug_script')
        xalign 0.9 yalign 0.3

    imagebutton:
        idle 'door_dark.png' hover 'door.png'
        action Jump('select')
        xalign 0.1 yalign 0.4



screen Day2:

    imagebutton:
        idle 'ivar/ivar_full_dark.png' hover 'ivar/ivar_full.png'
        action Jump('ivar_script')
        xalign 0.1 yalign 0.3

    imagebutton:
        idle 'tulbug/tulbug_full_dark.png' hover 'tulbug/tulbug_full.png'
        action Jump('tulbug_script')
        xalign 0.5 yalign 0.4

    imagebutton:
        idle 'helga/helga_full_dark.png' hover 'helga/helga_full.png'
        action Jump('helga_script')
        xalign 0.9 yalign 0.3


# 여기에서부터 게임이 시작합니다.
label start:
    scene white
    centered "{cps=20}전사들의 가장 힘든 점은 아무래도 음식이다.{vspace=20}
    바다에 오래 나가 있다 보면 요리를 하기 힘들기 때문이다.{vspace=20}
    그들에겐 긴 항해를 끝내고 먹는, 혹은 지친 몸을 달래줄 맛있는 음식이 필요하다.{vspace=20}
    {vspace=20}
    그게 내가 전사들이 사는 이 작은 마을에 식당을 연 이유다.{/cps}"

#2

    scene black 
    "(문두드리는 소리)"

    b " ......"

    "(문 두드리는 소리)"

    b "아침부터 누구지...."

    scene bg bg_river

    

    show tulbug_normal:
        xalign 0.9
        ypos 100
    with dissolve

    t "역시 있었군 비욘슨!"

    hide tulbug_normal
    show tulbug_normal_dark:
        xalign 0.9
        ypos 110

    show bjorsson_normal:
        xalign 0.1
        ypos 100
    with dissolve
   
    b "아, 툴부그씨,{vspace=20}
    아침부터 무슨 일이시죠? 식당을 열려면 아직 멀었는데..."

    hide bjorsson_normal
    show bjorsson_normal_dark:
        xalign 0.1
        ypos 110

    hide tulbug_normal_dark
    show tulbug_normal:
        xalign 0.9
        ypos 100

    t "이것좀 보게나-"

    hide tulbug_normal
    show tulbug_normal_dark:
        xalign 0.9
        ypos 110

    hide bjorsson_normal_dark
    show bjorsson_normal:
        xalign 0.1
        ypos 100
    with dissolve

    b "세상에, 직접 잡으신 거예요?"

    hide bjorsson_normal
    show bjorsson_normal_dark:
        xalign 0.1
        ypos 110

    hide tulbug_normal_dark
    show tulbug_normal:
        xalign 0.9
        ypos 100

    t "오늘 새벽에 낚았어, 이렇게 큰 녀석은 "

    hide tulbug_normal
    show tulbug_normal_dark:
        xalign 0.9
        ypos 110

    hide bjorsson_normal_dark
    show bjorsson_normal:
        xalign 0.1
        ypos 100
    with dissolve

    b "질이 정말 좋은데요, 손질만 잘하면 맛도 좋겠는걸요."

    hide bjorsson_normal
    show bjorsson_normal_dark:
        xalign 0.1
        ypos 110

    hide tulbug_normal_dark
    show tulbug_normal:
        xalign 0.9
        ypos 100

    t "요즘은 항해가 뜸해서 낚시할 시간이 많아. 덕분에 이녀석을 잡았지.{vspace=20}
    자 받게, 이거로 요리를 해줄 수 있겠어?"

    hide tulbug_normal
    show tulbug_normal_dark:
        xalign 0.9
        ypos 110

    hide bjorsson_normal_dark
    show bjorsson_normal:
        xalign 0.1
        ypos 100
    with dissolve

    b "이렇게 좋은 재료라면, 그냥 집에서 부인과 드시는게...."

    hide bjorsson_normal
    show bjorsson_normal_dark:
        xalign 0.1
        ypos 110

    hide tulbug_normal_dark
    show tulbug_normal:
        xalign 0.9
        ypos 100

    t "그거야 바로 그거, 그래서 자네에게 부탁하는거야."

    hide tulbug_normal
    show tulbug_normal_dark:
        xalign 0.9
        ypos 110

    hide bjorsson_normal_dark
    show bjorsson_normal:
        xalign 0.1
        ypos 100
    with dissolve

    b "...예?"

    hide bjorsson_normal
    show bjorsson_normal_dark:
        xalign 0.1
        ypos 110

    hide tulbug_normal_dark
    show tulbug_normal:
        xalign 0.9
        ypos 100

    t "자세한건 나중에 알려줄테니....{vspace=20}
    요리 해줄건가 말건가? 돈은 얼마든지 있네"

    hide tulbug_normal
    show tulbug_normal_dark:
        xalign 0.9
        ypos 110

    hide bjorsson_normal_dark
    show bjorsson_normal:
        xalign 0.1
        ypos 100
    with dissolve

    b "그렇게 말씀하신다면야.... "

    hide bjorsson_normal
    show bjorsson_normal_dark:
        xalign 0.1
        ypos 110

    hide tulbug_normal_dark
    show tulbug_normal:
        xalign 0.9
        ypos 100

    t "그럼 믿고 가겠네, 좀있다 보세-!"

    hide tulbug_normal
    show tulbug_normal_dark:
        xalign 0.9
        ypos 110

    hide bjorsson_normal_dark
    show bjorsson_normal:
        xalign 0.1
        ypos 100
    with dissolve

    "(그렇게 툴부그씨는 질 좋은 연어를 건네준 채 자리에 앉았다.)"

#select_day1
    label select_day1:
        scene bg bg_river
        call screen Day1


#tulbug
    label tulbug_script:
        scene bg_forest
        show tulbug_happy:
            xalign 0.9
            ypos 100

        show bjorsson_normal_dark:
            xalign 0.1
            ypos 110

        t "여 비욘슨, 요리는 아직인가?"

        menu:
            "이야기를 더 듣는다.":
                jump tulbug_script2
            "요리하러 간다":
                jump select_day1
#tulbug_script2
    label tulbug_script2:
        scene bg_forest
        show tulbug_happy_dark:
            xalign 0.9
            ypos 110

        show bjorsson_normal:
            xalign 0.1
            ypos 100

        b "아까 말씀하셨던 것 말인데요...."

        menu: 
            "연어에 관해 물어본다":
                jump tulbug_salmon
            "부인에 관해 물어본다":
                jump tulbug_wife
            "항해에 관해 물어본다":
                jump tulbug_sail

        jump select_day1

#tulbug_salmon
    label tulbug_salmon:
        scene bg_river
        show bjorsson_normal:
            xalign 0.1
            ypos 100
                
        show tulbug_happy_dark:
            xalign 0.9
            ypos 110

        b "갓 잡은 저 연어... 어떻게 요리해 드릴까요?"

        hide bjorsson_normal
        show bjorsson_normal_dark:
            xalign 0.1
            ypos 110

        hide tulbug_happy_dark
        show tulbug_happy:
            xalign 0.9
            ypos 100

        t "난 요리는 잘 몰라, 그냥 맛있게 부탁하네"

        hide bjorsson_normal_dark
        show bjorsson_normal:
            xalign 0.1
            ypos 100

        hide tulbug_happy
        show tulbug_happy_dark:
            xalign 0.9
            ypos 110

        b "....?"

        jump select_day1

#tulbug_wife
    label tulbug_wife:
        scene bg_river
        show bjorsson_normal:
            xalign 0.1
            ypos 100
                
        show tulbug_happy_dark:
            xalign 0.9
            ypos 110

        b "브렌다씨는 잘 지내시죠?"

        hide bjorsson_normal
        show bjorsson_normal_dark:
            xalign 0.1
            ypos 110

        hide tulbug_happy_dark
        show tulbug_happy:
            xalign 0.9
            ypos 100

        t "우리아내? 안그래도 곧 올때가 됐는데..."

        hide bjorsson_normal_dark
        show bjorsson_normal:
            xalign 0.1
            ypos 100

        hide tulbug_happy
        show tulbug_happy_dark:
            xalign 0.9
            ypos 110

        b "...?"

        hide bjorsson_normal
        show bjorsson_normal_dark:
            xalign 0.1
            ypos 110

        hide tulbug_happy_dark
        show tulbug_happy:
            xalign 0.9
            ypos 100

        t "연어말이야 연어, 우리 아내랑 같이 먹으려고,"

        jump select_day1

#select
    label select:
        menu:
            "요리를 진행하시겠습니까?":
                jump cook_day1
            "툴부그의 이야기를 더 들어보시겠습니까?":
                jump select_day1

#cook_day2
    label cook_day1:


    return
