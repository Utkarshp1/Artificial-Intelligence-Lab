/*
* @file botTemplate.cpp
* @author Arun Tejasvi Chaganty <arunchaganty@gmail.com>
* @date 2010-02-04
* Template for users to create their own bots
*/

#include <chrono>
#include<limits>
#include <utility>
#include <vector>
#include "Othello.h"
#include "OthelloBoard.h"
#include "OthelloPlayer.h"
#include <cstdlib>

using namespace std;
using namespace Desdemona;

auto start = chrono::steady_clock::now();
int time_taken(){
    return (chrono::duration_cast<chrono::milliseconds>(chrono::steady_clock::now() - start).count());
}

int minimum_int = std::numeric_limits<int>::min();
int maximum_int = std::numeric_limits<int>::max();

class MyBot: public OthelloPlayer
{
    public:
        /**
         * Initialisation routines here
         * This could do anything from open up a cache of "best moves" to
         * spawning a background processing thread. 
         */
        MyBot( Turn turn );

        /**
         * Play something 
         */
        virtual Move play( const OthelloBoard& board );
		virtual int minimax(OthelloBoard &board, int max_depth, Turn turn, int alpha, int beta, Move move);
		virtual int heuristic1(OthelloBoard &board);
		virtual int heuristic2(OthelloBoard &board);
		virtual int heuristic3(OthelloBoard &board);
    private:
};

MyBot::MyBot( Turn turn )
    : OthelloPlayer( turn )
{
}

Move MyBot::play( const OthelloBoard& board )
{
	/*
	* This functions returns the best move in 2 seconds for a particular heuristic
	*/

	start = chrono::steady_clock::now();

	/*
	* getValidMoves return the available moves for particular
	* state in the board storing these moves in a list 
	* they are children in our tree
	*/

    list<Move> moves = board.getValidMoves( turn );

    /* 
    * storing first move in iterator it 
    */

    list<Move>::iterator it = moves.begin();

    /* 
    * declaring some variable for getting best move,bestscore
    */

	Move best_move = *it;
	int best_score = minimum_int;
	int max_depth = 0;

	/*
	* iterating tree till it reaches either leaf node
	* or time becomes greater than 2 seconds
	*/

	for (; ; max_depth++) {
		list<Move>::iterator it = moves.begin();

		/*
		* iterating over all valid moves/childrens to get the best move
		*/

		for (; it != moves.end(); it++) {

			/* 
			* since OthelloBoard is a const so we can't change its value
			* so making copy of it for using it further
			*/

			OthelloBoard board_copy = OthelloBoard(board);

			/*
			* recursively finding the best move by applying minimax algorithm
			*/

			int value = minimax(board_copy, max_depth, this->turn, minimum_int, maximum_int, *it);
			// int value = 0;
			if (value == minimum_int) {
				return best_move;
			}
			
			if (best_score < value) {
				best_score = value;
				best_move = *it;
			}
		}
	}

    return best_move;
}

int MyBot::minimax(OthelloBoard &board, int max_depth, Turn turn, int alpha, int beta, Move move) {
	/*
	* The minimax algorithm searches the game tree till depth k
	* in a depth-first manner from left to right.
	* It applies the minimax rule to determine the value of the root node.
	* Once the algorithm reaches the terminal node,
	* the algorithm applies the evaluation function (heuristic function) 
	*instead of making a recursive call.
	*/

	/* 
	* If time becomes greater than 1.6 seconds we stops searching.
	*/

	if (time_taken() > 1600) {
		return minimum_int;
	}

	/* 
	* Making othelloboard copy to apply particular move and
	* and select best move recursively.
	*/

	OthelloBoard board_copy = OthelloBoard(board);
	board_copy.makeMove(turn, move);

	/*
	* Storing childrens in list of descendants
	*/

	list<Move> descendants = board_copy.getValidMoves(other(turn));
	

	if (max_depth != 0) {
		if (this->turn != turn) {
			int best = minimum_int;
			int depth = max_depth - 1;
			// Turn turn = other(turn);
			list<Move>::iterator it = descendants.begin();
			for (; it != descendants.end(); it++) {
				int value = minimax(board_copy, depth, other(turn), alpha, beta, *it);
				if (value != minimum_int) {
					if (value > best) {
						best = value;
					}
					if (best > alpha) {
						alpha = best;
					}
					if (alpha <= beta) {
						continue;
					}
					else {
						break;
					}
				}
				else {
					return minimum_int;
				}
			}
			return best;
		}
		else {
			int best = maximum_int;
			list<Move>::iterator it = descendants.begin();
			int depth = max_depth - 1;
			// Turn turn = other(turn);
			for (; it != descendants.end(); it++) {
				int value = minimax(board_copy, depth, other(turn), alpha, beta, *it);
				if (value < best) {
					best = value;
				}
				if (best < beta) {
					beta = best;
				}
				if (alpha <= beta) {
					continue;
				}
				else {
					break;
				}
			}
			return best;
		}
	}
	else {
		return heuristic1(board_copy);
		// return 0;
	}
}

int MyBot::heuristic1(OthelloBoard &board) {
	
	/*
	* In this heuristic we are calculating 
	* the difference between the number of RED coins on the board and the BLACK coins on the board.
	* Hence, this heuristic determines whether the player is leading or
	* falling behind in comparison to his/her opponent.
	*/

	if (this->turn == RED) {
		return (board.getRedCount() - board.getBlackCount());
	}
	else {
		return (board.getBlackCount() - board.getRedCount());
	}
}

int MyBot::heuristic2(OthelloBoard &board) {

	/* 
	* In the game of Othello, the corner positions are one of strongest positions.
	* The player who occupies more number of corner positions has a higher chance of winning.
	* Hence, this heuristic calculates the 
	* difference between the number of corners occupied by me and my opponent.
	*/

	vector <pair <int, int>> cor;
	cor.push_back(make_pair(0, 0));
	cor.push_back(make_pair(0, 7));
	cor.push_back(make_pair(7, 0));
	cor.push_back(make_pair(7, 7));
	Turn turn = this-> turn;
	int opposite_corners = 0;
	int my_corners = 0;
	
	for(unsigned int i=0; i<cor.size(); i++) {
		if (board.get(cor[i].first, cor[i].second) == other(turn)) {
			opposite_corners++;
		}
		else if (board.get(cor[i].first, cor[i].second) == turn) {
			my_corners++;
		}
	}
	return (my_corners - opposite_corners);
}

int MyBot::heuristic3(OthelloBoard &board) {

	/* 
	* The player who has a higher number of
	* available positions/moves than his/her opponent has higher chances of winning
	* as it is more likely that the move is better. 
	* Hence, this heuristic calculates the 
	* difference between the number of available moves for me and my opponent.
	*/

	return (board.getValidMoves(this->turn).size() - board.getValidMoves(other(this->turn)).size());
}


// The following lines are _very_ important to create a bot module for Desdemona

extern "C" {
    OthelloPlayer* createBot( Turn turn )
    {
        return new MyBot( turn );
    }

    void destroyBot( OthelloPlayer* bot )
    {
        delete bot;
    }
}


