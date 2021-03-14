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
	start = chrono::steady_clock::now();
    list<Move> moves = board.getValidMoves( turn );
    // int randNo = rand() % moves.size();
    list<Move>::iterator it = moves.begin();
	Move best_move = *it;
	int best_score = minimum_int;
	int max_depth = 0;
	for (; ; max_depth++) {
		list<Move>::iterator it = moves.begin();
		for (; it != moves.end(); it++) {
			OthelloBoard board_copy = OthelloBoard(board);
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
		// if (max_depth >= 2) {
			// return best_move;
		// }
	}

    return best_move;
}

int MyBot::minimax(OthelloBoard &board, int max_depth, Turn turn, int alpha, int beta, Move move) {
	if (time_taken() > 1600) {
		return minimum_int;
	}
	
	OthelloBoard board_copy = OthelloBoard(board);
	board_copy.makeMove(turn, move);
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
					// if (best > alpha) {
						// alpha = best;
					// }
					// if (alpha <= beta) {
						// continue;
					// }
					// else {
						// break;
					// }
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
				// if (best < beta) {
					// beta = best;
				// }
				// if (alpha <= beta) {
					// continue;
				// }
				// else {
					// break;
				// }
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
	if (this->turn == RED) {
		return (board.getRedCount() - board.getBlackCount());
	}
	else {
		return (board.getBlackCount() - board.getRedCount());
	}
}

int MyBot::heuristic2(OthelloBoard &board) {
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


