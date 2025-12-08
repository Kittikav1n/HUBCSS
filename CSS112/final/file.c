int main(){
    FILE *a;
    a = fopen("note.txt", "w");
    char name[1000];
    char note[1000];
    printf("input your name: ");
    fgets(name, sizeof(name), stdin);
    printf("input Note: ");
    fgets(note, sizeof(note), stdin);
    
    fprintf(a, "Name: %s\n", name);
    fprintf(a, "Note: %s", note);
    fclose(a);
}