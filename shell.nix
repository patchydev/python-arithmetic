let
  pkgs = import (fetchTarball("channel:nixpkgs-unstable")) {};
  in pkgs.mkShell {
    buildInputs = [ pkgs.python314 pkgs.python312Packages.pip ];
}