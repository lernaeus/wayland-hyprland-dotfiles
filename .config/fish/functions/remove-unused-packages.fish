function remove-unused-packages
paru -Qtdq | paru -Rns - $argv
end
