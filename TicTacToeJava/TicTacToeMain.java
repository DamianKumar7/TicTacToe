import java.util.*;
public class TicTacToeMain {
    Board currentBoard;
    Player player1;
    Player player2;
    Scanner sc;
    TicTacToeMain(){
        sc = new Scanner(System.in);
        currentBoard = new Board();
    }
    public static  void  main(String[]args){
        TicTacToeMain newGame = new TicTacToeMain();
        newGame.playGame();
    }
    public void playGame(){
        currentBoard.resetBoard();
        boolean gameOverSignal = false;
        int currentPlayerId = 1;
        while(!gameOverSignal){
            player1 = new Player("X");
            player2 = new Player("O");
        }
    }

}

