#!/usr/bin/awk -f

function parse() {
        
        count[$1" "$9]++
        
}

parse()

END {
        for (char in count)
        {
                print(count[char],char)|"sort -nru"
}
}