# 이 파일에 게임 스크립트를 입력합니다.

define gui.text_color = "#663f18"
define gui.text_font = "SCDream4.otf"


# image 문을 사용해 이미지를 정의합니다.
#image bg

image bg select_food1 = "1.png"
image bg bg_river = "background/bg_river.jpg"
image bg bg_forest = "background/bg_forest.jpg"
image bg bg_indoor = "background/bg_indoor.png"
image bg bg_outoor = "background/bg_outdoor.jpg"
image bg bg_outdoor_night = "background/bg_outdoor_night.jpg"
image bg bg_party = "background/bg_party.png"
image bg bg_ending1 = "background/bg_ending1.png"
image bg bg_nextday = "background/bg_nextday.png"
image bg bg_main = "background/bg_main.png"
image white = Solid("#ffffff")
image black = Solid("#000000")

#image human
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

image ivar_and_warriors="ivar/ivar_and_warriors.png"

image tulbug_happy:
    im.FactorScale("tulbug/tulbug_happy.png", 0.6)

image tulbug_happy_dark:
    im.FactorScale("tulbug/tulbug_happy_dark.png", 0.6)

image tulbug_normal:
    im.FactorScale("tulbug/tulbug_normal.png", 0.6)

image tulbug_normal_dark:
    im.FactorScale("tulbug/tulbug_normal_dark.png", 0.6)

image tulbug_angry:
    im.FactorScale("tulbug/tulbug_angry.png", 0.6)

image tulbug_angry_dark:
    im.FactorScale("tulbug/tulbug_angry_dark.png", 0.6)

#image object
image table_0:
    im.FactorScale("object/table_0.png", 0.6)
image pepper = "food/pepper.png"
image salmon:
    im.FactorScale("food/salmon.png", 0.5)
image beer = "food/beer.png"

image salmon_steak = "food/salmon_steak.png"


# 게임에서 사용할 캐릭터를 정의합니다.
define b = Character('비욘슨', color = "#ebd660", what_slow_cps = 20)
define c = Character('촌장', color = "#658c6a", what_slow_cps = 20)
define h = Character('헬가', color = "#862041", what_slow_cps = 20)
define i = Character('아이바르', color = "#467171", what_slow_cps =20)
define t = Character('툴부그', color = "#948d82", what_slow_cps = 20)

define tulbug_story = 0
define helga_on = False
define helga_story = 0
define ivar_story = 0

transform ib_fade:
        alpha 0.0
        easein 1.0 alpha 1.0


screen Day1:
    imagebutton:
        idle 'tulbug/tulbug_full_nofish_dark.png' hover 'tulbug/tulbug_full_nofish.png'
        action Jump('tulbug_script')
        xalign 0.8
        ypos 170
        at ib_fade


    imagebutton:
        idle 'object/table_0.png'
        xalign 0.5
        yalign 1.0
        at ib_fade

screen Day2:


    imagebutton:
        idle 'tulbug/tulbug_full_nofish_dark.png' hover 'tulbug/tulbug_full_nofish.png'
        action Jump('helga_tulbug')
        xalign 0.8
        ypos 170
        at ib_fade

    imagebutton:
        idle 'helga/helga_full_dark.png' hover 'helga/helga_full.png'
        action Jump('helga_script2')
        xalign 0.5
        ypos 170
        at ib_fade
    
    imagebutton:
        idle 'object/table_1.png'
        xalign 0.5
        yalign 1.0
        at ib_fade

screen Day3:

    imagebutton:
        idle 'tulbug/tulbug_full_nofish_dark.png' hover 'tulbug/tulbug_full_nofish.png'
        action Jump('ivar_tulbug')
        xalign 0.8
        ypos 170
        at ib_fade


    imagebutton:
        idle 'helga/helga_full_dark.png' hover 'helga/helga_full.png'
        action Jump('ivar_helga')
        xalign 0.47
        ypos 170
        at ib_fade

    imagebutton:
        idle 'ivar/ivar_full_dark.png' hover 'ivar/ivar_full.png'
        action Jump('ivar_script2')
        xalign 0.2
        ypos 140
        at ib_fade

    imagebutton:
        idle 'object/table_2.png'
        xalign 0.5
        yalign 1.0
        at ib_fade


# 여기에서부터 게임이 시작합니다.
label start:
    scene white
    with Dissolve(1.0)
    play music "audio/bgm/alexander-nakarada-fantasy-motion-loop-ready.mp3"
    centered "{cps=20}전사들의 가장 힘든 점은 아무래도 음식이다.{vspace=20}
    바다에 오래 나가 있다 보면 요리를 하기 힘들기 때문이다.{vspace=20}
    그들에겐 긴 항해를 끝내고 먹는, 혹은 지친 몸을 달래줄 맛있는 음식이 필요하다.{vspace=20}
    {vspace=20}
    그게 내가 전사들이 사는 이 작은 마을에 식당을 연 이유다.{/cps}"

#2

    scene black 
    play sound "audio/effect/99BA524C5CF6DE2D0E.mp3"
    with vpunch


    b " ......"

    play sound "audio/effect/99BA524C5CF6DE2D0E.mp3"
    with vpunch

    b " 아침부터 누구지...."

    scene bg bg_indoor

    

    show tulbug_normal:
        xalign 0.9
        ypos 100
    with dissolve

    t " 역시 있었군 비욘슨!"

    hide tulbug_normal
    show tulbug_normal_dark:
        xalign 0.9
        ypos 110

    show bjorsson_normal:
        xalign 0.1
        ypos 100
    with dissolve
   
    b " 아, 툴부그씨,{vspace=15}
    아침부터 무슨 일이시죠? 식당을 열려면 아직 멀었는데..."

    hide bjorsson_normal
    show bjorsson_normal_dark:
        xalign 0.1
        ypos 110

    hide tulbug_normal_dark
    show tulbug_normal:
        xalign 0.9
        ypos 100      

    t " 이것좀 보게나-"
    
    window hide dissolve

    scene black
    with fade

    show salmon:
        xalign 0.5
        ypos 300
    with dissolve

    $renpy.pause()

    hide salmon
    with dissolve

    scene bg_indoor


    show tulbug_normal_dark:
        xalign 0.9
        ypos 110


    show bjorsson_normal:
        xalign 0.1
        ypos 100
    with fade

    window show dissolve

    b " 세상에, 직접 잡으신 거예요?"

    hide bjorsson_normal
    show bjorsson_normal_dark:
        xalign 0.1
        ypos 110

    hide tulbug_normal_dark
    show tulbug_normal:
        xalign 0.9
        ypos 100

    t " 오늘 새벽에 낚았어, 이렇게 큰 녀석은 좀처럼 보기 힘들다고"

    hide tulbug_normal
    show tulbug_normal_dark:
        xalign 0.9
        ypos 110

    hide bjorsson_normal_dark
    show bjorsson_normal:
        xalign 0.1
        ypos 100

    b " 질이 정말 좋은데요, 손질만 잘하면 맛도 좋겠는걸요."

    hide bjorsson_normal
    show bjorsson_normal_dark:
        xalign 0.1
        ypos 110

    hide tulbug_normal_dark
    show tulbug_normal:
        xalign 0.9
        ypos 100

    t " 요즘은 항해가 뜸해서 낚시할 시간이 많아. 덕분에 이녀석을 잡았지.{vspace=15}
    자 받게, 이거로 요리를 해줄 수 있겠어?"

    hide tulbug_normal
    show tulbug_normal_dark:
        xalign 0.9
        ypos 110

    hide bjorsson_normal_dark
    show bjorsson_normal:
        xalign 0.1
        ypos 100

    b " 이렇게 좋은 재료라면, 그냥 집에서 부인과 드시는게...."

    hide bjorsson_normal
    show bjorsson_normal_dark:
        xalign 0.1
        ypos 110

    hide tulbug_normal_dark
    show tulbug_normal:
        xalign 0.9
        ypos 100

    t " 그거야 바로 그거, 그래서 자네에게 부탁하는거야."

    hide tulbug_normal
    show tulbug_normal_dark:
        xalign 0.9
        ypos 110

    hide bjorsson_normal_dark
    show bjorsson_normal:
        xalign 0.1
        ypos 100

    b " ...예?"

    hide bjorsson_normal
    show bjorsson_normal_dark:
        xalign 0.1
        ypos 110

    hide tulbug_normal_dark
    show tulbug_normal:
        xalign 0.9
        ypos 100

    t " 자세한건 나중에 알려줄테니....{vspace=15}
    요리 해줄건가 말건가? 돈은 얼마든지 있네"

    hide tulbug_normal
    show tulbug_normal_dark:
        xalign 0.9
        ypos 110

    hide bjorsson_normal_dark
    show bjorsson_normal:
        xalign 0.1
        ypos 100

    b " 그렇게 말씀하신다면야.... "

    hide bjorsson_normal
    show bjorsson_normal_dark:
        xalign 0.1
        ypos 110

    hide tulbug_normal_dark
    show tulbug_normal:
        xalign 0.9
        ypos 100

    t " 그럼 믿고 가겠네, 좀있다 보세-!"

    hide tulbug_normal
    show tulbug_normal_dark:
        xalign 0.9
        ypos 110

    hide bjorsson_normal_dark
    show bjorsson_normal:
        xalign 0.1
        ypos 100

    " (그렇게 툴부그씨는 질 좋은 연어를 건네준 채 자리에 앉았다.)"

    window hide dissolve

    jump select_day1

#select_day1
    label select_day1:
        scene bg bg_indoor
        with Fade(1.0, 1.0, 1.0)

        call screen Day1

#select_day2
    label select_day2:
        scene bg bg_indoor
        with Fade(1.0, 1.0, 1.0)

        call screen Day2

#select_day3
    label select_day3:
        scene bg bg_indoor
        with Fade(1.0, 1.0, 1.0)

        call screen Day3


#tulbug

    #tulbug_script
        label tulbug_script:
            scene bg_indoor
            show tulbug_happy:
                xalign 0.9
                ypos 100

            show bjorsson_normal_dark:
                xalign 0.1
                ypos 110
            with fade

            t " 여 비욘슨, 요리는 아직인가?"

        label tulbug_select:

            if tulbug_story==3:
                jump tulbug_end

            hide tulbug_happy
            show tulbug_happy_dark:
                xalign 0.9
                ypos 110

            hide bjorsson_normal_dark
            show bjorsson_normal:
                xalign 0.1
                ypos 100

            menu: 
                "연어에 관해 물어본다":
                    jump tulbug_salmon
                with dissolve

                "부인에 관해 물어본다":
                    jump tulbug_wife
                with dissolve

                "항해에 관해 물어본다":
                    jump tulbug_sail
                with dissolve

            jump select_day1
            
    #tulbug_salmon
        define tulbug_salmon_first=0
        label tulbug_salmon:
            scene bg_indoor
            show bjorsson_normal:
                xalign 0.1
                ypos 100
                    
            show tulbug_happy_dark:
                xalign 0.9
                ypos 110

            b " 갓 잡은 저 연어... 어떻게 요리해 드릴까요?"

            hide bjorsson_normal
            show bjorsson_normal_dark:
                xalign 0.1
                ypos 110

            hide tulbug_happy_dark
            show tulbug_happy:
                xalign 0.9
                ypos 100

            t " 난 요리는 잘 몰라, 그냥 맛있게 부탁하네"

            hide bjorsson_normal_dark
            show bjorsson_normal:
                xalign 0.1
                ypos 100

            hide tulbug_happy
            show tulbug_happy_dark:
                xalign 0.9
                ypos 110

            b " ....?"

            if tulbug_salmon_first==0:
                $tulbug_salmon_first=1
                $tulbug_story=tulbug_story+1

            jump tulbug_select

    #tulbug_wife
        define tulbug_wife_first=0
        label tulbug_wife:
            scene bg_indoor
            show bjorsson_normal:
                xalign 0.1
                ypos 100
                    
            show tulbug_happy_dark:
                xalign 0.9
                ypos 110

            b " 브렌다씨는 잘 지내시죠?"

            hide bjorsson_normal
            show bjorsson_normal_dark:
                xalign 0.1
                ypos 110

            hide tulbug_happy_dark
            show tulbug_happy:
                xalign 0.9
                ypos 100

            t " 우리아내? 안그래도 곧 올때가 됐는데..."

            hide bjorsson_normal_dark
            show bjorsson_normal:
                xalign 0.1
                ypos 100

            hide tulbug_happy
            show tulbug_happy_dark:
                xalign 0.9
                ypos 110

            b " ...?"

            hide bjorsson_normal
            show bjorsson_normal_dark:
                xalign 0.1
                ypos 110

            hide tulbug_happy_dark
            show tulbug_happy:
                xalign 0.9
                ypos 100

            t " 연어말이야 연어, 우리 아내랑 같이 먹으려고,"

            if tulbug_wife_first==0:
                $tulbug_wife_first=1
                $tulbug_story=tulbug_story+1

            jump tulbug_select

    #tulbug_sail
        define tulbug_sail_first=0
        label tulbug_sail:
            scene bg_indoor
            show bjorsson_normal:
                xalign 0.1
                ypos 100
                    
            show tulbug_happy_dark:
                xalign 0.9
                ypos 110

            b " 항해가 요즘 잘 안되세요?"

            hide bjorsson_normal
            show bjorsson_normal_dark:
                xalign 0.1
                ypos 110

            hide tulbug_happy_dark
            show tulbug_angry:
                xalign 0.9
                ypos 100

            t " 요즘 해적이 많아져서 말이야.. 빌어먹을 놈들.. {vspace=15}
            원래 갈 수 있던 항로의 반의 반도 못가게 됐어 에잉 쯧"

            hide bjorsson_normal_dark
            show bjorsson_normal:
                xalign 0.1
                ypos 100

            hide tulbug_angry
            show tulbug_angry_dark:
                xalign 0.9
                ypos 110

            b " 그거 참 큰일이네요..."

            hide bjorsson_normal
            show bjorsson_normal_dark:
                xalign 0.1
                ypos 110

            hide tulbug_angry_dark
            show tulbug_angry:
                xalign 0.9
                ypos 100

            t " 됐어 이런얘기는 말자구"

            hide bjorsson_normal_dark
            show bjorsson_normal:
                xalign 0.1
                ypos 100

            hide tulbug_angry
            show tulbug_angry_dark:
                xalign 0.9
                ypos 110

            b " ..."

            if tulbug_sail_first==0:
                $tulbug_sail_first=1
                $tulbug_story=tulbug_story+1


            jump tulbug_select

    #tulbug_end
        label tulbug_end:
            show bjorsson_normal:
                xalign 0.1
                ypos 100

            hide tulbug_angry_dark
            with dissolve

            hide tulbug_happy_dark
            with dissolve
    
            b " 툴부그씨에게 연어를 받았다."
            b " 연어 요리에 사용할 조미료가 없을까? {vspace=15} 밖에 나가보자"

            jump helga_script

#helga

    #helga_script
        $helga_on = True
        label helga_script:
            scene black
            with dissolve

            play sound "audio/effect/door_open.mp3"

            scene white
            with dissolve

            scene bg_outdoor
            with Dissolve(3.5)

            pause

            show bjorsson_normal:
                xalign 0.1
                ypos 100
            with dissolve

            window show dissolve

            b " 연어에 무슨 조미료가 어울리려나..."

            hide bjorsson_normal
            show bjorsson_normal_dark:
                xalign 0.1
                ypos 110

            show helga_happy:
                xalign 0.9
                ypos 100
            with dissolve

            "???" " 비욘슨씨~~~~"
            "???" " 오늘은 개점이 빠르네요~ 오늘의 메뉴는 뭔가요?"

            hide bjorsson_normal_dark
            show bjorsson_normal:
                xalign 0.1
                ypos 100

            hide helga_happy
            show helga_happy_dark:
                xalign 0.9
                ypos 110

            b " 아 헬가씨, 오늘은 툴부그씨가 좋은 연어를 가져와 주셨어요. {vspace=15}
            지금부터 조미료를 구하러 가는길이에요"

            hide bjorsson_normal
            show bjorsson_normal_dark:
                xalign 0.1
                ypos 110

            hide helga_happy_dark
            show helga_happy:
                xalign 0.9
                ypos 100
            
            h " 오 마침 제가 후추를 가져왔어요"

            window hide dissolve

            scene black
            with fade

            show pepper:
                xalign 0.5
                ypos 180
            with dissolve

            $renpy.pause()

            hide pepper
            with dissolve

            scene bg_outdoor
           
            show bjorsson_normal:
                xalign 0.1
                ypos 100
            
            show helga_happy_dark:
                xalign 0.9
                ypos 110
            with fade

            window show dissolve

            b " 이 귀한걸!!!! {vspace=15}
            어디서 구하셨어요?"

            hide bjorsson_normal
            show bjorsson_normal_dark:
                xalign 0.1
                ypos 110

            hide helga_happy_dark
            show helga_happy:
                xalign 0.9
                ypos 100

            
            h " 요전에 옆마을에서 방랑상인이 왔을때 얻었어요"

            hide bjorsson_normal_dark
            show bjorsson_normal:
                xalign 0.1
                ypos 100

            hide helga_happy
            show helga_happy_dark:
                xalign 0.9
                ypos 110

            b " 이렇게 귀한걸 그냥 받을 수 는 없어요..."

            hide bjorsson_normal
            show bjorsson_normal_dark:
                xalign 0.1
                ypos 110

            hide helga_happy_dark
            show helga_happy:
                xalign 0.9
                ypos 100
            
            h " 괜찮아요 오늘은 축제날이니까 다들 음식을 먹으러 올거에요. {vspace=15}
            맛있는 요리 기대하고 있을게요"

            hide bjorsson_normal_dark
            show bjorsson_normal:
                xalign 0.1
                ypos 100

            hide helga_happy
            show helga_happy_dark:
                xalign 0.9
                ypos 110

            b " ..."

            window hide dissolve

            jump select_day2

    #helga_script2
        label helga_script2:
            scene bg_indoor
            show helga_happy_dark:
                xalign 0.9
                ypos 110

            show bjorsson_normal:
                xalign 0.1
                ypos 100
            with fade

            b " 아까 말씀하셨던 것 말인데요...."

        label helga_select:

            if helga_story==3:
                jump helga_end

            if helga_pepper_first==1:
                menu: 
                    "후추에 관해 물어본다":
                        jump helga_pepper
                    with dissolve

                    "축제에 관해 물어본다":
                        jump helga_festival
                    with dissolve

                    "방랑상인에 관해 물어본다":
                        jump helga_merchant
                    with dissolve

            else:
                menu: 
                    "후추에 관해 물어본다":
                        jump helga_pepper
                    with dissolve

                    "축제에 관해 물어본다":
                        jump helga_festival
                    with dissolve

            jump select_day2

    #helga_pepper
        define helga_pepper_first=0
        label helga_pepper:
            scene bg_indoor
            show bjorsson_normal:
                xalign 0.1
                ypos 100
                    
            show helga_happy_dark:
                xalign 0.9
                ypos 110

            window show dissolve

            b " 후추는 어디서 얻으신거예요?"

            hide bjorsson_normal
            show bjorsson_normal_dark:
                xalign 0.1
                ypos 110

            hide helga_happy_dark
            show helga_happy:
                xalign 0.9
                ypos 100

            h " 저번에 옆마을에서 방랑상인이라는 사람이 왔길래 식사를 대접했더니{vspace=15}
            이 후추를 줬어요"

            hide bjorsson_normal_dark
            show bjorsson_normal:
                xalign 0.1
                ypos 100

            hide helga_happy
            show helga_happy_dark:
                xalign 0.9
                ypos 110

            b " ....?"
            
            window hide dissolve

            if helga_pepper_first==0:
                $helga_pepper_first=1
                $helga_story=helga_story+1

            jump helga_select

    #helga_festival
        define helga_festival_first=0
        label helga_festival:
            scene bg_indoor
            show bjorsson_normal:
                xalign 0.1
                ypos 100
                    
            show helga_happy_dark:
                xalign 0.9
                ypos 110

            window show dissolve

            b " 오늘이 축제날이었던가요?"

            hide bjorsson_normal
            show bjorsson_normal_dark:
                xalign 0.1
                ypos 110

            hide helga_happy_dark
            show helga_happy:
                xalign 0.9
                ypos 100

            h " 비욘슨씨도 참 내일이 전사들의 출정날이잖아요{vspace=15}
            출정날 전날은 항상 축제날이었는데 잊어버리신건가요?"

            hide bjorsson_normal_dark
            show bjorsson_normal:
                xalign 0.1
                ypos 100

            hide helga_happy
            show helga_happy_dark:
                xalign 0.9
                ypos 110

            b " '내일이 벌써 출정날이었나... '"

            window hide dissolve

            if helga_festival_first==0:
                $helga_festival_first=1
                $helga_story=helga_story+1

            jump helga_select

    #helga_merchant
        define helga_merchant_first=0
        label helga_merchant:
            scene bg_indoor
            show bjorsson_normal:
                xalign 0.1
                ypos 100
                    
            show helga_happy_dark:
                xalign 0.9
                ypos 110

            window show dissolve

            b " 방랑상인이 마을에 왔었던가요? "

            hide bjorsson_normal
            show bjorsson_normal_dark:
                xalign 0.1
                ypos 110

            hide helga_happy_dark
            show helga_happy:
                xalign 0.9
                ypos 100

            h " 산 기슭에서 봤는데 급한일이 있는지 식사를 하시고는 바로 가시더라구요"

            hide bjorsson_normal_dark
            show bjorsson_normal:
                xalign 0.1
                ypos 100

            hide helga_happy
            show helga_happy_dark:
                xalign 0.9
                ypos 110

            b " 음..?"

            hide bjorsson_normal
            show bjorsson_normal_dark:
                xalign 0.1
                ypos 110

            hide helga_happy_dark
            show helga_happy:
                xalign 0.9
                ypos 100

            h " 아 그러고 보니 출정날이 언제인지 물어봤었어요"

            window hide dissolve

            if helga_merchant_first==0:
                $helga_merchant_first=1
                $helga_story=helga_story+1
            

            jump helga_select

    #helga_tulbug
        label helga_tulbug:
            scene bg_indoor
            show tulbug_happy:
                xalign 0.1
                ypos 100
                    
            show helga_happy_dark:
                xalign 0.9
                ypos 110

            t " 아 헬가씨! 오면서 내 마누라 브렌다 못봤어요?"

            hide tulbug_happy
            show tulbug_happy_dark:
                xalign 0.1
                ypos 110

            hide helga_happy_dark
            show helga_happy:
                xalign 0.9
                ypos 100

            h " 아 봤어요 봤어요!! {vspace=15}  저희 집에서 수다떨고 있던데요!"

            hide tulbug_happy_dark
            show tulbug_normal:
                xalign 0.1
                ypos 100

            hide helga_happy
            show helga_happy_dark:
                xalign 0.9
                ypos 110

            t " 이 여편네, 저녁쯤이나 되어야 오겠군..."

            jump select_day2

    #helga_end
        label helga_end:

            hide helga_happy_dark
            with dissolve

            hide helga_happy
            with dissolve

            window show dissolve

            b "내일이 출정날이라면 이제 슬슬 전사들이 오겠군"

            window hide dissolve

            jump ivar_script


#ivar

    #ivar_script
        label ivar_script:
            scene bg_forest1
            play music "audio/bgm/My Mother Told Me (Vikings Anthem) Instrumental cover - Low Tin Whistle (Norse Flute Viking Music) (online-audio-converter.com).mp3" fadeout 3.0 fadein 0.5
            
            show ivar_and_warriors:
                xalign 0.5
                ypos 100
            with Fade(1.0, 1.0, 1.0)
            
            $renpy.pause(0.5)

            window show dissolve

            "???" "{cps=20} ~내 엄마는 나에게 말하곤 하셨지~{/cps}{w=2.5}{nw}"
            "???" "{cps=20} ~언젠가 먼 바다를 건널 좋은 노를 가진 갤리선을 사게 될 거라고~{/cps}{w=2.0}{nw}"
            "???" "{cps=20} ~뱃머리에 서서 안식처로 계속 나아가라~{/cps}{w=3.0}{nw}"
            "???" "{cps=20} ~수많은 적들의 머리를 쳐라~{/cps}{w=2.5}{nw}"
            "???" "{cps=20} ~수많은 적들의 머리를 쳐라~{/cps}{w=2.5}{nw}"


            scene bg_indoor

            hide bjorsson_normal_dark
            show bjorsson_normal:
                xalign 0.1
                ypos 100
            with fade

            b " 아 마침 전사분들이 오셨나봐요"

            play sound "audio/effect/door_slam.mp3"

            show ivar_happy:
                xalign 0.9
                ypos 100
            with vpunch

            hide bjorsson_normal
            show bjorsson_normal_dark:
                xalign 0.1
                ypos 110


            i " 그래 나 아이바르가 왔지 우리의 위대한 출정을 위해!!"

            hide bjorsson_normal_dark
            show bjorsson_normal:
                xalign 0.1
                ypos 100

            hide ivar_happy
            show ivar_happy_dark:
                xalign 0.9
                ypos 110

            b " 오오 아이바르씨! 전사분들도 오셨군요!"

            show ivar_happy:
                xalign 0.9
                ypos 100
            with vpunch

            hide bjorsson_normal
            show bjorsson_normal_dark:
                xalign 0.1
                ypos 110


            i " 비욘슨 이걸 받게 우리의 출정을 기념할 벌꿀주일세"


            window hide dissolve

            scene black
            with dissolve

            show beer:
                xalign 0.5
                ypos 150
            with dissolve

            $renpy.pause()

            hide beer
            with dissolve

            scene bg_indoor
           
            show bjorsson_normal:
                xalign 0.1
                ypos 100
            
            show ivar_happy_dark:
                xalign 0.9
                ypos 110
            with fade

            window show dissolve

            b " 이것 참 오늘은 특별한 밤이 되겠군요"

            window hide dissolve

            jump select_day3
            
    #ivar_script2
        label ivar_script2:
            scene bg_indoor
            show ivar_happy_dark:
                xalign 0.9
                ypos 110

            show bjorsson_normal:
                xalign 0.1
                ypos 100
            with fade

            b " 아이바르씨!"

        label ivar_select:

            if ivar_story==3:
                stop music fadeout 5.0
                jump ivar_end

            if ivar_tomorrow_first==1:
                menu: 
                    "벌꿀주에 관해 물어본다":
                        jump ivar_beer
                    with dissolve

                    "출정일에 관해 물어본다":
                        jump ivar_tomorrow
                    with dissolve

                    "준비에 관해 물어본다":
                        jump ivar_town
                    with dissolve

            else:
                menu: 
                    "벌꿀주에 관해 물어본다":
                        jump ivar_beer
                    with dissolve

                    "출정일에 관해 물어본다":
                        jump ivar_tomorrow
                    with dissolve

            jump select_day2

    #ivar_beer
        define ivar_beer_first=0
        label ivar_beer:
            scene bg_indoor
            show bjorsson_normal:
                xalign 0.1
                ypos 100
                    
            show ivar_happy_dark:
                xalign 0.9
                ypos 110

            b " 벌꿀주!!"

            hide bjorsson_normal
            show bjorsson_normal_dark:
                xalign 0.1
                ypos 110

            hide ivar_happy_dark
            show ivar_happy:
                xalign 0.9
                ypos 100

            i " 음!!"

            hide bjorsson_normal_dark
            show bjorsson_normal:
                xalign 0.1
                ypos 100

            hide ivar_happy
            show ivar_happy_dark:
                xalign 0.9
                ypos 110

            b " ....?"

            if ivar_beer_first==0:
                $ivar_beer_first=1
                $ivar_story=ivar_story+1

            jump ivar_select

    #ivar_tomorrow
        define ivar_tomorrow_first=0
        label ivar_tomorrow:
            scene bg_indoor
            show bjorsson_normal:
                xalign 0.1
                ypos 100
                    
            show ivar_happy_dark:
                xalign 0.9
                ypos 110

            b " 그나저나 출정일은 다음주라고 들었던것 같은데..."

            hide bjorsson_normal
            show bjorsson_normal_dark:
                xalign 0.1
                ypos 110

            hide ivar_happy_dark
            show ivar_normal:
                xalign 0.9
                ypos 100

            i " 아 그래 비욘슨 내가 말을 안했었군"
            i " 요전에 옆 마을에서 갑자기 출정일을 앞당겨서 말이지"

            hide ivar_normal
            show ivar_happy:
                xalign 0.9
                ypos 100

            i " 급하게 일정을 바꾸느라 준비가 조금 덜 되었지만 어떻게든 되겠지 하하하"

            hide bjorsson_normal_dark
            show bjorsson_normal:
                xalign 0.1
                ypos 100

            hide ivar_happy
            show ivar_happy_dark:
                xalign 0.9
                ypos 110

            b " ....?"

            if ivar_tomorrow_first==0:
                $ivar_tomorrow_first=1
                $ivar_story=ivar_story+1

            jump ivar_select

    #ivar_town
        define ivar_town_first=0
        label ivar_town:
            scene bg_indoor
            show bjorsson_normal:
                xalign 0.1
                ypos 100
                    
            show ivar_happy_dark:
                xalign 0.9
                ypos 110

            b " 참고로 준비가 덜된건 뭔가요?"

            hide bjorsson_normal
            show bjorsson_normal_dark:
                xalign 0.1
                ypos 110

            hide ivar_happy_dark
            show ivar_happy:
                xalign 0.9
                ypos 100

            i " 출정동안 마을을 지킬 병력을 못구했어..."

            hide bjorsson_normal_dark
            show bjorsson_normal:
                xalign 0.1
                ypos 100

            hide ivar_happy
            show ivar_happy_dark:
                xalign 0.9
                ypos 110

            b " 음...."

            if ivar_town_first==0:
                $ivar_town_first=1
                $ivar_story=ivar_story+1

            jump ivar_select
    
    #ivar_tulbug
        label ivar_tulbug:

            
    #ivar_helga
        label ivar_helga:

    #ivar_end
        label ivar_end:
            scene bg_indoor
            show bjorsson_normal:
                xalign 0.1
                ypos 100
            with dissolve
    
            b "슬슬 사람들도 모일 것 같다"
            b "요리를 준비하자"

            jump party_script

#party

    #party_script
        label party_script:
            scene black
            with Dissolve(3.0)

            $renpy.pause(1.0)

            play sound "audio/effect/knife_slicing.mp3"

            $renpy.pause()

            b "음?!?"

            play sound "audio/effect/frying_chips.mp3"
            $renpy.pause()
            b "호오....."

            play sound "audio/effect/shaker.mp3"
            $renpy.pause()
            b "!!!"

            play sound "audio/effect/success.mp3"
            show salmon_steak:
                xalign 0.5
                ypos 180
            with dissolve

            $renpy.pause()

            hide salmon
            with dissolve

            scene bg_party
            with Fade(1.0,1.0,1.0)

            play music "audio/bgm/crowd_talking.mp3" fadein 1.0

            $renpy.pause(3.0)

            show ivar_happy:
                xalign 0.5
                ypos 100
            with dissolve
            with vpunch

            i "건배!!! 우리의 위대한 출정을 위하여!!"

            "전사들" "{cps=20}우오오오오오!!!!{/cps}"

            hide ivar_happy
            with Dissolve(2.0)

            $renpy.pause()

            show tulbug_angry:
                xalign 0.5
                ypos 100
            with dissolve

            t "이놈의 여편네는 아직도 안오고 뭐하는거야!!"

            hide tulbug_angry
            with Dissolve(2.0)

            $renpy.pause()

            show helga_happy:
                xalign 0.5
                ypos 100
            with dissolve

            h "음~ 너무 맛있어 다음에는 다른 향신료를 드려봐야겠어 후훗"

            hide helga_happy
            with Dissolve(2.0)

            $renpy.pause()

            show bjorsson_normal:
                xalign 0.5
                ypos 100
            with dissolve

            b "..."

            scene black
            with Dissolve(2.0)

            play sound "audio/effect/door_open.mp3"

            stop music fadeout 3.0
            play music "audio/bgm/crowd_talking_small.mp3" fadein 1.0

            scene bg_outdoor_night
            with dissolve

            window show dissolve

            b "후..."
            b "다들 맛있게 먹어주니 기분이 좋군"
            b "일단 요리는 했는데 뭔가 찜찜하단 말이지...."
            b "..."

            window hide dissolve

            menu: 
                "기분탓이다":
                    jump ending_1
                with dissolve

                "뭔가가 이상하다":
                    jump ending_2
                with dissolve


#ending

    #ending_1
    label ending_1:
        scene bg_outdoor_night
        
        window show dissolve

        b "그래 당장 내일이 출정인데 분위기 깨기도 좀 그렇고 기분탓이겠지..."

        window hide dissolve

        play music "audio/bgm/sea_waves.mp3" fadeout 2.0 fadein 3.0

        scene black
        with Dissolve(2.0)

        $renpy.pause(5.0)

        scene bg_nextday
        with Dissolve(2.0)

        $renpy.pause(2.0)

        scene black
        with Dissolve(2.0)

        $renpy.pause(2.0)
        
        show ivar_and_warriors:
            xalign 0.5
            ypos 100
        with Dissolve(2.0)
        
        i "'음... 뭔가 이상하군... 분명 옆마을 전사들이 올 시간이 지났는데...'"

        i "일단 마을로 돌아가자!!"with vpunch

        "전사들" "{cps=20}넵!!!!{/cps}"

        scene bg_ending1
        with Fade(1.0,1.0,5.0)

        centered "{cps=20}{color=#ffffff}마을은 어째서인지 불길에 휩싸여 있었다.{vspace=20}
        아이바르와 전사들은 서둘러 마을에 돌아왔지만{vspace=20}
        그들이 할 수 있는것은 죽은자들의 시신을 정리해주는것 뿐이었다.{vspace=20}{/color}{/cps}"

        jump end
      
    #ending_2
    label ending_2:
        scene bg_outdoor_night

        window show dissolve

        b " 해적이며, 방랑상인이며, 옆마을이며 뭔가 이상하단 말이지{vspace=15}
        아이바르씨에게 말을 해봐야겠어"

        window hide

        scene black
        with Dissolve(2.0)

        scene bg_party
        with Dissolve(2.0)

        scene bg_indoor

        show bjorsson_normal:
            xalign 0.1 
            ypos 110

        show ivar_normal_dark:
            xalign 0.9
            ypos 100
        with fade

        b " 아이바르씨 아무래도 불안해요"
        b " 툴부그씨가 요즘 근해에 해적인지 뭔지 항로를 막고 있대요"
        b " 헬가씨는 방랑상인이 와서 우리 출정일을 물어보고 갔대요{vspace=15}
        저는 상인들이 오면 식재료를 사야해서 대부분 알고 있는데 {vspace=15} 최근에 방랑상인이 왔다는 소식은 듣지를 못했어요"
        b " 마지막으로 급하게 출정일을 바꾸게 한 옆마을이 수상해요"
        b " 죄송하지만 출정일을 미뤄주셨으면 좋겠어요..."

        hide bjorsson_normal
        show bjorsson_normal_dark:
            xalign 0.1
            ypos 100

        hide ivar_normal_dark
        show ivar_normal:
            xalign 0.9
            ypos 110

        i " 흠... 아니야 비욘슨 미안할 필요는 없네"
        i " 나도 툴부그씨나 헬가씨가 말한 정보는 몰랐네{vspace=15}
        그렇게 들으니 상당히 수상하군"
        i " 자네가 말한대로 하겠네 다른 전사들에게는 내가 말하지"

        window hide dissolve

        scene black
        with Dissolve(2.0)

        stop music fadeout 1.0

        scene bg_nextday
        with Dissolve(2.0)

        

        scene bg_forest
        with Dissolve(2.0)


        show ivar_and_warriors:
            xalign 0.5
            ypos 100
        with dissolve
        
        window show dissolve

        "전사" "{cps=20} 아이바르님 말씀하신대로 이쪽협곡으로 옆마을 전사들이 들어왔습니다!!!{/cps}"

        i " 그래 믿고 싶진 않았는데 역시 그랬군..."

        i " ..."

        i " 전사들!!!! 일제사격!!!!"with vpunch

        window hide Dissolve(1.0)

        play music "audio/bgm/alexander-nakarada-fantasy-motion-loop-ready.mp3"

        scene bg_main
        with Dissolve(4.0)

        centered "{cps=20}{vspace=400}{color=#ffffff}바이킹의 전사들은 항상 삶과 죽음의 경계에 있다.{vspace=20}
        약탈을 한다는 것은 언제나 약탈당할 각오를 하는 것이다.{vspace=50}
        항상 경계하면 살아가야하는 전사들에게도{vspace=20} 
        맛있는 음식과 잠시 쉬어갈 장소는 필요하다.{vspace=50}
        그게 내가 전사들이 사는 이 작은 마을에 식당을 연 이유다.{/color}{/cps}"

        jump end

    label end:
        scene black
        with Dissolve(10.0)


            



            



