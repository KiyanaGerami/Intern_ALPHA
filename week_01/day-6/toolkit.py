APP_NAME = "terminal-toolkit"
VERSION = "0.1.0"
LINE = "=" * 40

print(LINE)
print(f"{APP_NAME + ' v' + VERSION: ^40}")
print(LINE)


while True:
    print()
    print("[1] Unit converter")
    print("[2] Tip calculator")
    print("[3] Text stats")
    print("[q] Quit")
    choice = input("> ").strip().lower()
    
    if choice == "1":
        print("-- Unit converter --")
        print("options: c2f, f2c, km2mi, mi2km, kg2lb, lb2kg")
        kind = input("conversion: ").strip().lower()
        value = float(input("value: "))
        if kind == "c2f":
            result = value * 9 / 5 + 32
            print(f"{value:.2f} C = {result:.2f} F")
        elif kind == "f2c":
            result = (value - 32) * 5 /9
            print(f"{value:.2f} F = {result:.2f} C")
        elif kind == "km2mi":
            result = value * 0.621371
            print(f"{value:.2f} Km = {result:.2f} Mi")
        elif kind == "mi2km":
            result = value / 0.621371
            print(f"{value:.2f} Mi = {result:.2f} Km")
        elif kind == "kg2lb":
            result = value * 2.20462
            print(f"{value:.2f} Kg = {result:.2f} Lb")
        elif kind == "lb2kg":
            result = value / 2.20462
            print(f"{value:.2f} Lb = {result:.2f} Kg")

        else: 
            print (f"unknown conversion: {kind}")
            
    elif choice == "2":
        print("-- Tip calculator --")
        total = float(input("enter total price: "))
        tip_percent =  int(input("enter percent of tip: "))
        person = int(input("enter number of people: "))
        
        tip = total * tip_percent / 100
        print(f"tip: {tip:,.2f}")
        total += tip
        print(f"total price is {total:,.2f}")
        each_person = total / person
        print(f"each person pays: {each_person:,.2f}")
        
        
    elif choice == "3":
        print("-- Text stats --")
        text = input("Enter your text: ")
        char_with_space = len(text)
        char_without_space = len(text.replace(" ", ""))
        import re
        words = re.findall(r'\b\w+\b', text)
        word_count = len(words)
        if word_count > 0:
            total_word_lengths = sum(len(word) for word in words)
            average_word_length = total_word_lengths / word_count
        else:
            average_word_length = 0
        if words:
            longest_word = max(words, key=len)
        else:
            longest_word = "None"   
        sentences = re.findall(r'[.!?]+', text)
        sentence_count = len(sentences)
        if word_count > 0:
            reading_time_seconds = (word_count / 200) * 60
            reading_time_seconds = max(1, round(reading_time_seconds)) 
        else:
            reading_time_seconds = 0
            
        print(f"Characters (with spaces): {char_with_space:,}")
        print(f"Characters (without spaces): {char_without_space:,}")
        print(f"Word count: {word_count}")
        print(f"Average word length: {average_word_length:.1f}")
        print(f"Longest word: {longest_word}")
        print(f"Sentence count: {sentence_count}")
        print(f"Estimated reading time: {reading_time_seconds} seconds")   
            
    elif choice == "q":
        print ("Goodbye from terminal-toolkit. Keep shipping!")
        break

    else:
        print(f" '{choice}' is not a valid option.")
