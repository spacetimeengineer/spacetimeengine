#!/usr/bin/env python
from spacetimeengine.solutions import *
from spacetimeengine.spacetime import *


def main():
    
    # Retrieves a known solution from the Solutions() class.
    blackhole = Solution().schwarzschild()
    
    # The current general model for describing the accellerated expansion of the universe.
    expanding_universe = Solution().friedmann_lemaitre_robertson_walker()
    
    # The most famous wormhole solution.
    wormhole = Solution().einstein_rosen_bridge()
    
    # Empty vacuum.
    flat_spacetime = Solution().minkowski()
    
    # A special case of a more general form of the Friedmann Lemaitre Robertson Walker solution.
    empty_expanding_universe = Solution().milne()
    
    # Gravity as we know it, without the high order effects.
    newtonian_gravity = Solution().weak_field_approximation()
    
    newtonian = SpaceTime(Solution().hypersphere_II())

if __name__ == "__main__":
    main()
