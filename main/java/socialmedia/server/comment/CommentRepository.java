package socialmedia.server.comment;

import org.springframework.data.jpa.repository.JpaRepository;
import socialmedia.server.post.Post;

import java.util.List;

public interface CommentRepository extends JpaRepository<Comment, Integer> {

    List<Comment> findByPost(Post post);  // Obține comentarii pentru o anumită postare
}
