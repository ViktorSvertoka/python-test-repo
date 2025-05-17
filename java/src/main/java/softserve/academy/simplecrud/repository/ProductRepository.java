package softserve.academy.simplecrud.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import softserve.academy.simplecrud.model.entity.Product;

public interface ProductRepository extends JpaRepository<Product, Long> {
}