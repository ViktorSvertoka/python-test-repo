using Microsoft.EntityFrameworkCore;
using Products.Models;

namespace Products.DataAccess
{
    public class ProductsContext : DbContext
    {
        public ProductsContext(DbContextOptions<ProductsContext> contextOptions) : base(contextOptions)
        { }
        public DbSet<Product> Products { get; set; }
    }
}
