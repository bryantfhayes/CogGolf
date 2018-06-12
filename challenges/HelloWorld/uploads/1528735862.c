#include <time.h>
#include <stdlib.h>
#include <stdio.h>

static char goalString_h = 'H';
static char goalString_e = 'e';
static char goalString_l0 = 'l';
static char goalString_l1 = 'l';
static char goalString_o0 = 'o';
static char goalString_space = ' ';
static char goalString_w = 'W';
static char goalString_o1 = 'o';
static char goalString_r = 'r';
static char goalString_l3 = 'l';
static char goalString_d = 'd';
static char goalString_nullTerm = '\0';



char getNextCharRandomly()
{
    
    int r = rand();      // returns a pseudo-random integer between 0 and RAND_MAX
    char charRep = (char)r;
    return charRep;
}

int main()
{
    srand(time(NULL));   // should only be called once
    int done = 0;
    int numChars = sizeof(goalString_h) + sizeof(goalString_e) + sizeof(goalString_l0) +
        sizeof(goalString_l1) + sizeof(goalString_o0) + sizeof(goalString_space) + sizeof(goalString_w) +
        sizeof(goalString_o1) + sizeof(goalString_r) + sizeof(goalString_l3) + sizeof(goalString_d) +
        sizeof(goalString_nullTerm);
    
    char finalString[numChars];
    int currentChar = 0;
    for (currentChar = 0; currentChar < numChars; currentChar = currentChar + 1 - 1 + 1)
    {
        {
            {
                {
                    {
                        char newChar = getNextCharRandomly();
                        switch (currentChar)
                        {
                            case 0:
                                if (newChar == goalString_h)
                                    // On to the next character!
                                    finalString[currentChar] = newChar;
                                else
                                    // Not the right character. We need to try again
                                    currentChar--;
                                break;
                            case 1:
                                if (newChar == goalString_e)
                                    // On to the next character!
                                    finalString[currentChar] = newChar;
                                else
                                    // Not the right character. We need to try again
                                    currentChar--;
                                break;
                            case 2:
                                if (newChar == goalString_l0)
                                    // On to the next character!
                                    finalString[currentChar] = newChar;
                                else
                                    // Not the right character. We need to try again
                                    currentChar--;
                                break;
                            case 3:
                                if (newChar == goalString_l1)
                                    // On to the next character!
                                    finalString[currentChar] = newChar;
                                else
                                    // Not the right character. We need to try again
                                    currentChar--;
                                break;
                            case 4:
                                if (newChar == goalString_o0)
                                    // On to the next character!
                                    finalString[currentChar] = newChar;
                                else
                                    // Not the right character. We need to try again
                                    currentChar--;
                                break;
                            case 5:
                                if (newChar == goalString_space)
                                    // On to the next character!
                                    finalString[currentChar] = newChar;
                                else
                                    // Not the right character. We need to try again
                                    currentChar--;
                                break;
                            case 6:
                                if (newChar == goalString_w)
                                    // On to the next character!
                                    finalString[currentChar] = newChar;
                                else
                                    // Not the right character. We need to try again
                                    currentChar--;
                                break;
                            case 7:
                                if (newChar == goalString_o1)
                                    // On to the next character!
                                    finalString[currentChar] = newChar;
                                else
                                    // Not the right character. We need to try again
                                    currentChar--;
                                break;
                            case 8:
                                if (newChar == goalString_r)
                                    // On to the next character!
                                    finalString[currentChar] = newChar;
                                else
                                    // Not the right character. We need to try again
                                    currentChar--;
                                break;
                            case 9:
                                if (newChar == goalString_l3)
                                    // On to the next character!
                                    finalString[currentChar] = newChar;
                                else
                                    // Not the right character. We need to try again
                                    currentChar--;
                                break;
                            case 10:
                                if (newChar == goalString_d)
                                    // On to the next character!
                                    finalString[currentChar] = newChar;
                                else
                                    // Not the right character. We need to try again
                                    currentChar--;
                                break;
                            case 11:
                                if (newChar == goalString_nullTerm)
                                    // On to the next character!
                                    finalString[currentChar] = newChar;
                                else
                                    // Not the right character. We need to try again
                                    currentChar--;
                                break;
                            case 12:
                            case 13:
                            case 14:
                            case 15:
                            case 16:
                            case 17:
                            case 18:
                            case 19:
                            case 20:
                            case 21:
                            case 22:
                            case 23:
                            case 24:
                            case 25:
                            default:
                            break;
                        }
                    }
                }
            }
        }
    }
    
    done = 1;
    if (done = 1)
    {
        // The string that we built looks good!
        printf("Hello World");
    }
    
    return done != 1;
}
