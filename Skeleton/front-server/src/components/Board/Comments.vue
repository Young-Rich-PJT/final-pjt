<template>
  <div>
    <h3>댓글</h3>
    <div>
      <label for="content"></label>
      <input type="text" class="content-box" id="content" v-model="content" @keyup.enter="createComment">
      <button type="submit" class="btn btn-success" id="content" @click="createComment">작성</button>
    </div>

    <br>
    <template v-if="commentList && commentList.filter(comment => comment.article === article.id).length === 0">
      <p>댓글이 없습니다.</p>
    </template>
    <template v-else>
      <p v-for="(comment, idx) in commentList" :key="idx" v-if="comment.article === article?.id">
        <span v-if="!editingCommentId || editingCommentId !== comment.id">
          <span class="comment-info">
            댓글 {{comment?.username}} : {{ comment?.content }}
          </span>
          <span class="comment-buttons">
            <button class="edit-button" @click="editComment(comment)">수정</button>
            <button class="delete-button" @click="deleteComment(comment)">삭제</button>
          </span>
        </span>
        <span v-else class="comment-wrapper">
          <input type="text" class="edit-input" v-model="editedContent">
          <button class="confirm-button" @click="updateComment(comment)">확인</button>
          <button class="cancel-button" @click="cancelEdit">취소</button>
        </span>
      </p>
    </template>
  </div>
</template>

<script>
import axios from 'axios';
const API_URL = 'http://127.0.0.1:8000';

export default {
  name: 'Comments',
  data() {
    return {
      content: null,
      commentList: this.$store.state.comments,
      editingCommentId: null,
      editedContent: ''
    };
  },
  props: {
    article: Object
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin;
    },
    userInfo() {
      return this.$store.state.user;
    }
  },
  created() {
    this.getComments();
  },
  methods: {
    deleteComment(comment) {
      axios({
        method: 'delete',
        url: `${API_URL}/api/v1/comments/${comment.id}/`
      })
        .then((response) => {
          console.log(response);
          this.getComments();
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getComments() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/comments/`
      })
        .then((res) => {
          if (res.status === 404) {
            console.log('fuck');
          }
          this.commentList = res.data;
        })
        .catch((err) => {
          this.commentList = null;
        });
    },
    createComment() {
      const content = this.content;
      if (this.content) {
        axios({
          method: 'post',
          url: `${API_URL}/api/v1/articles/${this.article.id}/comments/`,
          data: { content },
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
        })
          .then(() => {
            this.content = null;
            this.getComments();
          })
          .catch((err) => {
            console.log(err);
          });
      } else {
        alert('댓글을 입력하세요!');
      }
    },
    editComment(comment) {
      this.editingCommentId = comment.id;
      this.editedContent = comment.content;
    },
    updateComment(comment) {
      axios({
        method: 'put',
        url: `${API_URL}/api/v1/articles/${this.article.id}/comments/`,
        data: {
          content: this.editedContent
        }
      })
        .then(() => {
          this.editingCommentId = null;
          this.editedContent = '';
          this.getComments();
        })
        .catch((err) => {
          console.log(err);
        });
    },
    cancelEdit() {
      this.editingCommentId = null;
      this.editedContent = '';
    }
  }
};
</script>

<style scoped>
.content-box {
    padding: 10px;
    background-color: #fff;
    border: 1px solid #ccc;
    border-radius: 5px;
  }

.comment-wrapper {
  display: flex;
  align-items: center;
}

.comment-info {
  flex: 1;
}

.comment-buttons {
  display: flex;
  align-items: center;
}

.comment-buttons button {
  margin-left: 10px;
  padding: 3px 6px;
  font-size: 12px;
  border-radius: 3px;
}

.delete-button {
  background-color: #dc3545;
  color: #fff;
  border: none;
}

.edit-button {
  background-color: #17a2b8;
  color: #fff;
  border: none;
}

.edit-input {
  width: 150px;
  padding: 3px 6px;
  border-radius: 3px;
  border: 1px solid #ccc;
}

.confirm-button {
  background-color: #28a745;
  color: #fff;
  border: none;
}

.cancel-button {
  background-color: #ffc107;
  color: #212529;
  border: none;
}
</style>
