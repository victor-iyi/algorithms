#include <cmath>
#define MAX_GRID 8

struct King {
  size_t x, y;

  King(size_t x, size_t y) : x(x), y(y) {}
};

struct Queen {
  size_t x, y;

  Queen(size_t x, size_t y) : x(x), y(y) {}
};

bool validate(const King& K, const Queen& Q) {
  return (K.x < MAX_GRID || K.y < MAX_GRID || Q.x < MAX_GRID || Q.y < MAX_GRID);
}

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
