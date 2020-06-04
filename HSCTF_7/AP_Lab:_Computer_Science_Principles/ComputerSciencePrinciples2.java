public class ComputerSciencePrinciples2
{
    public static void main(String[] args) {
        String inp = "inagzgkpm)Wl&Tg&io";
        if (inp.length()!=18) {
            System.out.println("Your input is incorrect.");
            System.exit(0);
        }
        inp=shift(shift2(inp));
        if (inp.equals("inagzgkpm)Wl&Tg&io")) {
            System.out.println("Correct. Your input is the flag.");
        }
        else {
            //System.out.println("Your input is incorrect.");
        }
        System.out.println(inp);
    }
    public static String shift(String input) {
        String ret = "";
        for (int i = 0; i<input.length(); i++) {
            ret+=(char)(input.charAt(i)+i);
        }
        return ret;
    }
    public static String shift2(String input) {
        String ret = "";
        for (int i = 0; i<input.length(); i++) {
            ret+=(char)(input.charAt(i)-Integer.toString((int)input.charAt(i)).length());
        }
        return ret;
    }
}
