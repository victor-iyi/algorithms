/** The Checkmate Problem.
 *
 * @description
 *  Given a King and a Queen, find out if the King is being
 *  threatened by the Queen.
 *
 * @solution
 *   The King is threatened by the Queen if 3 conditions are satisfied:
 *    1. Horizontally:
 *          King.x == Queen.x
 *    2. Vertically:
 *          King.y == Queen.y
 *    3. Diagonally:
 *          abs(King.x - Queen.x) == abs(King.y - Queen.y)
 *
 * @author
 *   Victor I. Afolabi
 *   Artificial Intelligence & Software Engineer.
 *   Email: javafolabi@gmail.com
 *   GitHub: https://github.com/victor-iyiola
 *
 * @project
 *   File: checkmate.cc
 *   Created on 26 August, 2018 @ 09:22 AM.
 *
 * @license
 *   MIT License
 *   Copyright (c) 2018. Victor I. Afolabi. All rights reserved.
 **/

#include <cmath>

// Maximum grid of a classic chess board.
#define MAX_GRID 8

struct King {
  size_t x, y;

  King(size_t x, size_t y) : x(x), y(y) {}
};

struct Queen {
  size_t x, y;

  Queen(size_t x, size_t y) : x(x), y(y) {}
};

/** Validate if the co-ordinates for King and Queen are out of bounds.
 *
 * @params
 *  K King&: King object.
 *  Q Queen&: Queen object.
 *
 * @return
 *    bool -- True if one of Queen or King is out of bounds,
 *            False, otherwise.
 */
bool validate(const King& K, const Queen& Q) {
  return (K.x < MAX_GRID || K.y < MAX_GRID || Q.x < MAX_GRID || Q.y < MAX_GRID);
}

/** Checkmate: Is King threatened by Queen?
 *
 * @params
 *  King& K: King object.
 *  Queen& Q: Queen object.
 *
 * @return
 *    bool -- True, if King is being threatened,
 *            False otherwise or co-ordinates out-of-bounds.
 */
bool checkmate(const King& K, const Queen& Q) {
  // Conditions:
  //    K.x == Q.x                  -- Horizontally
  //    K.y == Q.y                  -- Vertically
  //    |K.x - Q.x| == |K.y - Q.y|  -- Diagonally
  if (validate(K, Q))
    return (K.x == Q.x || K.y == Q.y ||
            std::abs(static_cast<float>(K.x - Q.x)) ==
                std::abs(static_cast<float>(K.y - Q.y)));

  return false;
}
