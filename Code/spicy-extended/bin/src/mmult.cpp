#include "mmult.h"

void mmult(int32_t a[4],int32_t b[4],int32_t c[4],std::unodered_map<std::string, std::string> x,int32_t size) {
   for(int i=0; i<(int)2; i=i+1) {
      for(int j=0; j<(int)2; j=j+1) {
         for(int k=0; k<(int)2; k=k+1) {
            c[(i)*2+j]+=(a[(i)*2+k]*b[(k)*2+j]);
         }
      }
   }
}
