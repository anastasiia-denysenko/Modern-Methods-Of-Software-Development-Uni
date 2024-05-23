class ref_and_point_zero
{
    public:
        int x = 5;
        const int& ref = x;
};
class ref_and_point_one
{
    public:
        int x = 10;
};
class ref_and_point_two
{
    public:
       const int& ref = 20;
};
int main()
{
  return 0;
}
