import java.util.*;
public  class Player{
    Scanner sc;
    Player(){
        sc = new Scanner();
    }
    public  int takePositionAsInputFromConsole(){
        System.out.println("Take Position From Board Where You Want To Place The Item");
        int positionOnBoard = sc.nextInt();
        return positionOnBoard;
    }

}