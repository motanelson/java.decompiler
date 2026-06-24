public class fchars {
    private static char charss(char a,char b){
        return (char)(a+b);
    }
    public static void main(String[] args) {
        char a=charss('A',(char)0x20);
        System.out.println(a);
    }
}
