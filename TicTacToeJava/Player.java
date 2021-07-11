import java.util.*;
public  class Player{
    Scanner sc;
    char playerPiece;
    Player(char playerPiece){
        sc = new Scanner();
        this.playerPiece = playerPiece;
    }
    public  int takePositionAsInputFromConsole(){
        System.out.println("Take Position From Board Where You Want To Place The Item");
        int positionOnBoard = sc.nextInt();
        return positionOnBoard;
    }

}