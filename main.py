#include <iostream>
using namespace std;

int user_input, number_enter_give, deposite_input;
string user_friends[] = {"Main", "Ahmed", "Mostafa", "Omar"}, friend_choose;
int moeny_in_the_bank[] = {2000, 3000, 5000, 20};

void showChoose()
{

    cout << "\n===================================" << endl;
    cout << "===========Bank Account Cpp APP=====" << endl;
    cout << "=====================================" << endl;
    cout << "==-1 Gimme me money==" << endl;
    cout << "==-2 Enter money==" << endl;
    cout << "==-3 give someone money==" << endl;
    cout << "==-4 how mutch i have ==" << endl;
    cout << "==-5 Exit ==" << endl;
    cout << "\nSelect Your choise : " << endl;
    cin >> user_input;
}

void procress()
{

    do
    {
        showChoose();
        switch (user_input)
        {

        case 1:

            cout << "You Choose : 1" << endl;
            cout << "You have in the bank : " << moeny_in_the_bank[0] << endl;
            cout << "How mutch do you want? : " << endl;
            cin >> number_enter_give;
            if (number_enter_give > moeny_in_the_bank[0])
            {
                cout << "you don't have that amount of moeny\n";
                procress();
            } // if break
            else
            {
                cout << "You Enter : " << number_enter_give << endl
                     << endl;
                moeny_in_the_bank[0] -= number_enter_give;
                cout << "process done! and your balance now " << moeny_in_the_bank[0] << endl
                     << endl;
            } // else
            break;
        case 2:
            cout << "You Choose : 2" << endl;
            cout << "You have in the bank : " << moeny_in_the_bank[0] << endl;
            cout << "How mutch do you want to deposite : " << endl;
            cin >> deposite_input;
            cout << "You enter : " << deposite_input << endl;
            moeny_in_the_bank[0] += deposite_input;
            cout << "process done! and your balance now " << moeny_in_the_bank[0] << endl
                 << endl;
            break;
        case 3:
            cout << "You Choose : 3" << endl;
            cout << "You have in the bank : " << moeny_in_the_bank[0] << endl;
            cout << "You have : ";
            for (int i = 1; i < size(user_friends); i++)
            {
                cout << i << "-" << user_friends[i] << " ";
            }
            cout << "\n";
            cout << "Choose Your Friend : " << endl;
            int friend_choose;
            cin >> friend_choose;
            // string choose = user_friends[i];
            cout << "How mutch do you want to give him : " << endl;
            int give;
            cin >> give;
            moeny_in_the_bank[friend_choose] += give;
            moeny_in_the_bank[0] -= give;
            cout << "you Transfare : " << give << "$\n";
            cout << "And Your balance : " << moeny_in_the_bank[0] << "$" << endl;
            break;
        case 4:
            cout << "You have in the bank : " << moeny_in_the_bank[0] << endl;

        } // switch case

    } while (user_input < 5);
}

int main()
{
    procress();
}

// WHITE
