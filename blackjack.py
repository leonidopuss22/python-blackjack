import random
def returncards(array:list):
    result = ""
    for i in array:
        result += f"{i}  "
    return result 

cmdin = str(input("Начать игру - start\nЗакончить игру - exit\n"))
if cmdin == "start":
    blackjack_cards = [
        '♠️ 2',
        '♣️ 2',
        '♦️ 2',
        '♥️ 2',
        '♠️ 3',
        '♣️ 3',
        '♦️ 3',
        '♥️ 3',
        '♠️ 4',
        '♣️ 4',
        '♦️ 4',
        '♥️ 4',
        '♠️ 5',
        '♣️ 5',
        '♦️ 5',
        '♥️ 5',
        '♠️ 6',
        '♣️ 6',
        '♦️ 6',
        '♥️ 6',
        '♠️ 7',
        '♣️ 7',
        '♦️ 7',
        '♥️ 7',
        '♠️ 8',
        '♣️ 8',
        '♦️ 8',
        '♥️ 8',
        '♠️ 9',
        '♣️ 9',
        '♦️ 9',
        '♥️ 9',
        '♠️ 10',
        '♣️ 10',
        '♦️ 10',
        '♥️ 10',
        '♠️ J',
        '♣️ J',
        '♦️ J',
        '♥️ J',
        '♠️ Q',
        '♣️ Q',
        '♦️ Q',
        '♥️ Q',
        '♠️ K',
        '♣️ K',
        '♦️ K',
        '♥️ K',
        '♠️ A',
        '♣️ A',
        '♦️ A',
        '♥️ A'
        
    ]
    random_start_card_player1 = random.choice(blackjack_cards)
    random_start_card_player2 = random.choice(blackjack_cards)
    while random_start_card_player2 == random_start_card_player1:
        random_start_card_player2 = random.choice(blackjack_cards)
    start_card_player = [random_start_card_player1, random_start_card_player2]

    random_start_card_bot1 = random.choice(blackjack_cards)
    while random_start_card_bot1 in start_card_player:
        random_start_card_bot1 = random.choice(blackjack_cards)
    random_start_card_bot2 = random.choice(blackjack_cards)
    while random_start_card_bot2 == random_start_card_bot1 or random_start_card_bot2 in start_card_player:
        random_start_card_bot2 = random.choice(blackjack_cards)
    start_card_bot = [random_start_card_bot1, random_start_card_bot2]

    player_points = 0
    for i in start_card_player:
        if i in blackjack_cards[:4]:
            player_points += 2
        elif i in blackjack_cards[4:8]:
            player_points += 3
        elif i in blackjack_cards[8:12]:
            player_points += 4
        elif i in blackjack_cards[12:16]:
            player_points += 5
        elif i in blackjack_cards[16:20]:
            player_points += 6
        elif i in blackjack_cards[20:24]:
            player_points += 7
        elif i in blackjack_cards[24:28]:
            player_points += 8
        elif i in blackjack_cards[28:32]:
            player_points += 9
        elif i in blackjack_cards[32:-4]:
            player_points += 10
        else:
            if player_points + 11 > 21:
                player_points += 1
            else:
                player_points += 11

    bot_points = 0
    for i in start_card_bot:
        if i in blackjack_cards[:4]:
            bot_points += 2
        elif i in blackjack_cards[4:8]:
            bot_points += 3
        elif i in blackjack_cards[8:12]:
            bot_points += 4
        elif i in blackjack_cards[12:16]:
            bot_points += 5
        elif i in blackjack_cards[16:20]:
            bot_points += 6
        elif i in blackjack_cards[20:24]:
            bot_points += 7
        elif i in blackjack_cards[24:28]:
            bot_points += 8
        elif i in blackjack_cards[28:32]:
            bot_points += 9
        elif i in blackjack_cards[32:-4]:
            bot_points += 10
        else:
            if bot_points + 11 > 21:
                bot_points += 1
            else:
                bot_points += 11

    bot_points_hovered = 0
    if True:
        if start_card_bot[0] in blackjack_cards[:4]:
            bot_points_hovered += 2
        elif start_card_bot[0] in blackjack_cards[4:8]:
            bot_points_hovered += 3
        elif start_card_bot[0] in blackjack_cards[8:12]:
            bot_points_hovered += 4
        elif start_card_bot[0] in blackjack_cards[12:16]:
            bot_points_hovered += 5
        elif start_card_bot[0] in blackjack_cards[16:20]:
            bot_points_hovered += 6
        elif start_card_bot[0] in blackjack_cards[20:24]:
            bot_points_hovered += 7
        elif start_card_bot[0] in blackjack_cards[24:28]:
            bot_points_hovered += 8
        elif start_card_bot[0] in blackjack_cards[28:32]:
            bot_points_hovered += 9
        elif start_card_bot[0] in blackjack_cards[32:-4]:
            bot_points_hovered += 10
        else:
            if bot_points_hovered + 11 > 21:
                bot_points_hovered += 1
            else:
                bot_points_hovered += 11 
    print(f"====================================\nВаши карты:\n{start_card_player[0]}  {start_card_player[1]}\n{player_points}\nКарты крупье:\n{start_card_bot[0]}  ?\n{bot_points_hovered}\n take - взять карту\n skip - пропустить\n")
    if player_points == 21:
        print("====================================\nПобеда!")
        print(f"Ваши карты: {start_card_player[0]}  {start_card_player[1]}\nОчки: BlackJack")
        print(f"Карты крупье: {start_card_bot[0]}  ?\nОчки: {bot_points_hovered}\n")
        game_over = True
    elif bot_points == 21: 
        print("====================================\nПоражение!")
        print(f"Ваши карты:{start_card_player[0]}  {start_card_player[1]}\nОчки: {player_points}")
        print(f"Карты крупье:{start_card_bot[0]}  {start_card_bot[1]}\nОчки: BlackJack\n")
        game_over = True
        
    game_over = False
    while cmdin != "quit" and not game_over:
        cmdin = str(input())
        if cmdin == "take":
            used_cards = []
            a = random.choice(blackjack_cards)
            for i in start_card_player:
                used_cards.append(i)
            for i in start_card_bot:
                used_cards.append(i)
            for i in used_cards:
                if a == i:
                    a = random.choice(blackjack_cards)
            start_card_player.append(a)
            player_points = 0
            for i in start_card_player:
                if i in blackjack_cards[:4]:
                    player_points += 2
                elif i in blackjack_cards[4:8]:
                    player_points += 3
                elif i in blackjack_cards[8:12]:
                    player_points += 4
                elif i in blackjack_cards[12:16]:
                    player_points += 5
                elif i in blackjack_cards[16:20]:
                    player_points += 6
                elif i in blackjack_cards[20:24]:
                    player_points += 7
                elif i in blackjack_cards[24:28]:
                    player_points += 8
                elif i in blackjack_cards[28:32]:
                    player_points += 9
                elif i in blackjack_cards[32:-4]:
                    player_points += 10
                else:
                    if player_points + 11 > 21:
                        player_points += 1
                    else:
                        player_points += 11
            
            if player_points > 21:
                print("====================================\nПоражение!")
                print(f"Ваши карты:{returncards(start_card_player)}\nОчки: {player_points}")
                print(f"Карты крупье:{start_card_bot[0]}  ?\nОчки: {bot_points_hovered}\n")
                game_over = not game_over
            elif player_points == 21:
                print("====================================\nПобеда!")
                print(f"Ваши карты:{returncards(start_card_player)}\nОчки: {player_points}")
                print(f"Карты крупье:{start_card_bot[0]}  ?\nОчки: {bot_points_hovered}\n")
                game_over = not game_over
            else:
                print(f"====================================\n take - взять карту\n skip - пропустить")
                print(f"Ваши карты:{returncards(start_card_player)}\nОчки: {player_points}")
                print(f"Карты крупье:{start_card_bot[0]}  ?\nОчки: {bot_points_hovered}\n")
                
                
        elif cmdin == "skip":
            used_cards = []
            for i in start_card_player:
                used_cards.append(i)
            for i in start_card_bot:
                used_cards.append(i)
            bot_points = 0
        
            while bot_points < 17:
                
                bot_points = 0
            
                for i in start_card_bot:
                    if i in blackjack_cards[:4]:
                        bot_points += 2
                    elif i in blackjack_cards[4:8]:
                        bot_points += 3
                    elif i in blackjack_cards[8:12]:
                        bot_points += 4
                    elif i in blackjack_cards[12:16]:
                        bot_points += 5
                    elif i in blackjack_cards[16:20]:
                        bot_points += 6
                    elif i in blackjack_cards[20:24]:
                        bot_points += 7
                    elif i in blackjack_cards[24:28]:
                        bot_points += 8
                    elif i in blackjack_cards[28:32]:
                        bot_points += 9
                    elif i in blackjack_cards[32:-4]:
                        bot_points += 10
                    else:
                        if bot_points + 11 > 21:
                            bot_points += 1
                        else:
                            bot_points += 11
                
                if bot_points >= 17:
                    break
                a = random.choice(blackjack_cards)
                for i in used_cards:
                    if a == i:
                        a = random.choice(blackjack_cards)
                start_card_bot.append(a)
                used_cards.append(a)
                
                
                
                
            
            bot_points = 0
            for i in start_card_bot:
                if i in blackjack_cards[:4]:
                    bot_points += 2
                elif i in blackjack_cards[4:8]:
                    bot_points += 3
                elif i in blackjack_cards[8:12]:
                    bot_points += 4
                elif i in blackjack_cards[12:16]:
                    bot_points += 5
                elif i in blackjack_cards[16:20]:
                    bot_points += 6
                elif i in blackjack_cards[20:24]:
                    bot_points += 7
                elif i in blackjack_cards[24:28]:
                    bot_points += 8
                elif i in blackjack_cards[28:32]:
                    bot_points += 9
                elif i in blackjack_cards[32:-4]:
                    bot_points += 10
                else:
                    if bot_points + 11 > 21:
                        bot_points += 1
                    else:
                        bot_points += 11
            
            player_points = 0
            for i in start_card_player:
                if i in blackjack_cards[:4]:
                    player_points += 2
                elif i in blackjack_cards[4:8]:
                    player_points += 3
                elif i in blackjack_cards[8:12]:
                    player_points += 4
                elif i in blackjack_cards[12:16]:
                    player_points += 5
                elif i in blackjack_cards[16:20]:
                    player_points += 6
                elif i in blackjack_cards[20:24]:
                    player_points += 7
                elif i in blackjack_cards[24:28]:
                    player_points += 8
                elif i in blackjack_cards[28:32]:
                    player_points += 9
                elif i in blackjack_cards[32:-4]:
                    player_points += 10
                else:
                    if player_points + 11 > 21:
                        player_points += 1
                    else:
                        player_points += 11
            if bot_points > 21:
                print("====================================\nПобеда!")
                print(f"Ваши карты:{returncards(start_card_player)}\nОчки: {player_points}")
                print(f"Карты крупье:{returncards(start_card_bot)}\nОчки: {bot_points}\n")
                game_over = not game_over
            elif bot_points > player_points:
                print("====================================\nПоражение!")
                print(f"Ваши карты:{returncards(start_card_player)}\nОчки: {player_points}")
                print(f"Карты крупье:{returncards(start_card_bot)}\nОчки: {bot_points}\n")
                game_over = not game_over
            elif bot_points == player_points:
                print("====================================\nНичья!")
                print(f"Ваши карты:{returncards(start_card_player)}\nОчки: {player_points}")
                print(f"Карты крупье:{returncards(start_card_bot)}\nОчки: {bot_points}\n")
                game_over = not game_over
        else:
            if cmdin == "exit":
                break
            else:
                print("Неверный ввод! take или skip!")
                continue
    print("Игра окончена")
else:
    print("Выход из игры, ожидалось start")