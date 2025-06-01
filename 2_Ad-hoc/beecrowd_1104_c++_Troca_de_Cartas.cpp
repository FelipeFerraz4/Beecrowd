#include <iostream>
#include <algorithm>
#include<set>

int main(){
    int number_cards_alici = -1, number_cards_beatriz = -1;
    do{
        std::cin >> number_cards_alici >> number_cards_beatriz;
        if(number_cards_alici == 0 && number_cards_beatriz == 0){
            break;
        }
        
        std::set<int> alici_cards;
        std::set<int> beatriz_cards;
        
        for(int i = 0; i < number_cards_alici; i++){
            int card;
            std::cin >> card;
            alici_cards.insert(card);
        }
        
        for(int i = 0; i < number_cards_beatriz; i++){
            int card;
            std::cin >> card;
            beatriz_cards.insert(card);
        }
        
        int only_alici = 0;
        int only_beatriz = 0;
        
        for(auto card : alici_cards){
            if(beatriz_cards.count(card) == 0){
                only_alici++;
            }
        }
        
        for(auto card : beatriz_cards){
            if(alici_cards.count(card) == 0){
                only_beatriz++;
            }
        }
        
        std::cout << std::min(only_alici, only_beatriz) << std::endl;
        
    }while(number_cards_alici != 0 || number_cards_beatriz != 0);
    
    return 0;
}
