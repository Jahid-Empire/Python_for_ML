ICT = ["ICE", "Geometry", "C", "C++", "Web"]
Biomedical = ["Gene", "Protien", "3D Image"]
Bangla = ["Kazi", "Rabindra", "Ahosan Habib"]

userInput = input("Enter Subject Name: ")
if userInput in ICT:
    print(f"The subject {userInput} is in ICT Department.")
elif userInput in Biomedical:
    print(f"The subject {userInput} is in Biomedical Department.")
elif userInput in Bangla:
    print(f"The subject {userInput} is in Bangla Department.")
else:
    print("Sorry to say, I can't help.")
