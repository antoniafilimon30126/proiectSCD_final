package socialmedia.server.comment;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class CommentService {

    @Autowired
    private CommentRepository commentRepository;

    // CREATE - Creare comentariu
    public Comment createComment(Comment comment) {
        return commentRepository.save(comment);
    }

    // READ - Obține toate comentariile
    public List<Comment> getAllComments() {
        return commentRepository.findAll();
    }

    // READ - Obține comentariul după ID
    public Optional<Comment> getCommentById(Integer id) {
        return commentRepository.findById(id);
    }

    // UPDATE - Actualizare comentariu
    public Comment updateComment(Integer id, Comment commentDetails) {
        Comment existingComment = commentRepository.findById(id).orElseThrow(() -> new RuntimeException("Comment not found for id: " + id));

        // Actualizează câmpurile comentariului
        existingComment.setContent(commentDetails.getContent());
        existingComment.setPost(commentDetails.getPost());
        existingComment.setUser(commentDetails.getUser());

        return commentRepository.save(existingComment);
    }

    // DELETE - Șterge comentariu
    public void deleteComment(Integer id) {
        Comment existingComment = commentRepository.findById(id).orElseThrow(() -> new RuntimeException("Comment not found for id: " + id));
        commentRepository.delete(existingComment);
    }
}
