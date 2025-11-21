
def diez(width, height):
    string=""
    for i in range(width):
        for j in range(height):
            if i == 0 or i==(width-1) or j==0 or j == (height-1):
                string+="#"
            else:
               string+=" "
        string+="\n"
    print(string)

diez(20, 20)    