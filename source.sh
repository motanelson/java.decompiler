printf "\e[47;31m\give me the java file of source no extension?"
read a
javac $a.java 
javap -private -c $a.class > $a.s