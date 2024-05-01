function rebuild-packages
checkrebuild | awk '{print $NF}' | paru -S - --rebuild $argv
end
