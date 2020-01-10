for i in *.png;
do
	convert "$i" -fuzz 7% -trim "$i";
done
